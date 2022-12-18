import json


class BotMainDB:
    with open("near/database/main.json", "r", encoding="utf-8") as file:
        embed = json.load(file)

    MESSAGE_PREFIX = embed["MESSAGE_PREFIX"]
    BOT_CREATOR_NAME = embed["BOT_CREATOR_NAME"]
    BOT_VERSION = embed["BOT_VERSION"]
    DEV_ID = embed["DEV_ID"]
    DEV_AND_OWNERS = embed["DEV_AND_OWNERS"]
