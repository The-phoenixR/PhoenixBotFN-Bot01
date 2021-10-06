import json
import random
import re
import requests

base_url = "https://fortnite-api.com/v2/"

def params_to_url(params: dict):
    result = []
    for k, v in params.items():
        if v is not None:
            result.append(f"{k}={v}")
    return "&".join(result)

ALT = {
    # regex formar | all lower cased | incasesensitive
    "matchMethod": {
        r"full|exact": "full",
        r"starts*|startswith": "starts",
        r"contains": "contains",
        r"ends*|endswith": "ends"
    },
    "type": {
        r"skin|outfit|character": "outfit",
        r"backpack|backbling|rucksack": "backpack",
        r"pickaxe": "pickaxe",
        r"contrail": "contrail",
        r"emote|dance": "emote",
        r"emoji|emojicon|sticker": "emoji",
        r"spray": "spray",
        r"loading[ _\-]?screen": "loading_screen"
    }
}


class API:
    def search(params: dict, only_id: bool = True, get_all_items: bool = False):
        url = base_url + f"cosmetics/br/search{'/all' if get_all_items else ''}?"
        payload = {}
        not_given = list(params.keys())
        for paramkey, paramvalue in params.items():
            if paramkey in ALT:
                for altkey, altvalue in ALT[paramkey].items():
                    if re.fullmatch(altkey, paramvalue, flags = re.I):
                        payload[paramkey] = altvalue
                        not_given.remove(paramkey)
                        break
            else:
                payload[paramkey] = paramvalue
                not_given.remove(paramkey)
        for p in not_given:
            payload[p] = None
        r = requests.get(url + params_to_url(payload))
        data = json.loads(r.text)["data"]
        if only_id and get_all_items:
            return [c["id"] for c in data]
        elif get_all_items:
            return data
        return data["id"] if only_id else data
    
    def random(params: dict, only_id: bool = True, allow_built_in: bool = False):
        cosmetic = random.choice(API.search(params, only_id, get_all_items = True))
        return cosmetic

if __name__ == "__main__":
    cosmetic = API.search({
        "name": "Roller Vibes",
        "type": "emote"
    }, False)
    print(cosmetic["gameplayTags"])
    
    cosmetic = API.random({
        "type": "emote"
    })
    print(cosmetic)
