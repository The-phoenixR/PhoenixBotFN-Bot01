from api import API

import asyncio

from dotenv import dotenv_values

import fortnitepy as fnpy

from fortnitepy.ext import commands

import json

import toml

import typeof

from modules import session

env = dotenv_values("assets/.env")

with open("assets/config/bot.toml", "r") as f:

    cfg = toml.loads(f.read())

auth = fnpy.DeviceAuth(

    device_id = env["DEVICE_ID"],

    account_id = env["ACCOUNT_ID"],

    secret = env["SECRET"]

)

PREFIX = cfg["bot"]["prefix"]

emote_interval = cfg["bot"]["emote_interval"]

bot = commands.Bot(

    PREFIX,

    auth

    #owner_ids = 0,

)

#me = bot.party.me

help_cmd = commands.HelpCommand(

    context = "help",

    command_prefix = PREFIX,

)

do_party = True

with session.Session("assets/log/") as s:

    # // EVENTS

    

    @bot.event

    async def event_ready():

        print("BOT ONLINE!")

        

        #me.set_avatar(avatar)

    

    @bot.event

    async def event_is_closed():

        pass

    

    @bot.event

    async def event_friend_message(message):

        author = message.author

        msg = message.content

        s.write_to_log(f"DM from '{author}': '{msg}'")

    

    @bot.event

    async def event_party_message(message):

        author = message.author

        msg = message.content

        s.write_to_log(f"PM from '{author}': '{msg}'")

    

    # // COMMANDS

    # ALPHAPETIC ORDER !

    

    @bot.command(name = "clown")

    async def cmd_clown(ctx):

        me = bot.party.me

        await me.set_emoji("Emoji_Clown")

    

    @bot.command(name = "confused")

    async def cmd_confused(ctx):

        me = bot.party.me

        await me.set_emoji("Emoji_S15_FutureSamurai")

    

    @bot.command(name = "cosmetic")

    async def cmd_cosmetic(ctx, name):

        cosmetics = get_cosmetics(name, f_type = "outfit")

    

    @bot.command(name = "emoji")

    async def cmd_emoji(ctx, name):

        me = bot.party.me

        await me.set_emote(API.search({"name": name, "type": "emoji"}))

    

    @bot.command(name = "emote")

    async def cmd_emote(ctx, name):

        me = bot.party.me

        await me.set_emote(API.search({"name": name, "type": "emote"}))

    

    @bot.command(name = "floss")

    async def cmd_floss(ctx):

        me = bot.party.me

        await me.set_emote("EID_Floss")

    

    @bot.command(name = "intro")

    async def cmd_intro(ctx):

        me = bot.party.me

        await me.set_outfit("CID_920_Athena_Commando_M_PartyTrooper")

        await me.set_emote("EID_Butter_1R26Q")

        await asyncio.sleep(5)

        await me.set_emote("EID_KingEagle")

    

    @bot.command(name = "kill")

    #@command.is_owner()

    async def cmd_kill(ctx):

        s.write_to_log("Bot killed")

        await bot.close()

    

    @bot.command(name = "locker")

    async def cmd_locker(ctx, name):

        me = bot.party.me

        with open(f"assets/lockers/{name}.locker.json") as f:

            data = json.loads(f.read())

            await me.set_outfit(API.search({"name": data["skin"], "type": "skin"}))

            await me.set_backpack(API.search({"name": data["backpack"], "type": "backpack"}))

            await me.set_pickaxe(API.search({"name": data["pickaxe"], "type": "pickaxe"}))

            await me.set_emote("EID_IceKing")

            await asyncio.sleep(4)

            await me.set_emote(API.search({"name": data["emote"], "type": "emote"}))

    

    @bot.command(name = "looser")

    async def cmd_looser(ctx):

        me = bot.party.me

        await me.set_emote("EID_TakeTheL")

    

    @bot.command(name = "love")

    async def cmd_love(ctx):

        me = bot.party.me

        await me.set_emoji("EID_TrueLove")

    

    @bot.command(name = "party")

    async def cmd_party(ctx, rarity = "*", no_repeat: Typeof.boolean = False):

        global do_party

        me = bot.party.me

        while do_party:

            if rarity != "*":

                emote = API.random({"type": "emote", "displayRarity": rarity}, False)

            else:

                emote = API.random({"type": "emote"}, False)

            if "Cosmetics.UserFacingFlags.BuiltInEmote" in emote["gameplayTags"]:

                continue

            await me.set_emote(emote["id"])

            await asyncio.sleep(emote_interval)

        do_party = True

    

    @bot.command(name = "pickaxe")

    async def cmd_pickaxe(ctx, name):

        me = bot.party.me

        await me.set_pickaxe(API.search({"name": name, "type": "pickaxe"}))

    

    @bot.command(name = "point")

    async def cmd_point(ctx):

        me = bot.party.me

        await me.set_emote("EID_IceKing")

    

    @bot.command(name = "realistic")

    async def cmd_realistic(ctx):

        me = bot.party.me

    

    @bot.command(name = "rickdance")

    async def cmd_rickdance(ctx):

        me = bot.party.me

        me.set_emote("EID_Ruckus")

        me.set_emote("EID_NeverGonna")

    

    @bot.command(name = "skin")

    async def cmd_skin(ctx, name):

        me = bot.party.me

        await me.set_outfit(API.search({"name": name, "type": "skin"}))

    

    @bot.command(name = "stopparty")

    async def cmd_stopparty(ctx):

        global do_party

        do_party = False

    

    @bot.command(name = "thumbsdown")

    async def cmd_thumbsdown(ctx):

        me = bot.party.me

        await me.set_emote("EID_ThumbsDown")

    

    @bot.command(name = "thumbsup")

    async def cmd_thumbsup(ctx):

        me = bot.party.me

        await me.set_emote("EID_ThumbsUp")

    

    @bot.command(name = "wow")

    async def cmd_wow(ctx):

        me = bot.party.me

        await me.set_emoji("Emoji_S15_Lexa")

    

    @bot.command(name = "yes")

    async def cmd_yes(ctx):

        me = bot.party.me

        me.set_emoji("")

    

    

    bot.run()

print("BOT OFFLINE")
