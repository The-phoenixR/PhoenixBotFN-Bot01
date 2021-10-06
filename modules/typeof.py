boolean(arg):
    if arg.lower() in "true|t|yes|y|1|enable|enabled|on".split("|"):
        return True
    elif arg.lower() in "false|f|no|n|0|diable|disabled|off".split("|"):
        return False
