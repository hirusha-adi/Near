import json
import typing as t
from loguru import logger
from . import db
from pocketbase.models.record import Record

class SettingsMain:
    with open("near/database/main.json", "r", encoding="utf-8") as file:
        embed = json.load(file)
    MESSAGE_PREFIX = embed["MESSAGE_PREFIX"]
    BOT_CREATOR_NAME = embed["BOT_CREATOR_NAME"]
    BOT_VERSION = embed["BOT_VERSION"]
    DEV_ID = embed["DEV_ID"]
    DEV_AND_OWNERS = embed["DEV_AND_OWNERS"]
    logger.debug("Loaded all primary settings from near/database/main.json")


class SettingsEmbeds:
    @staticmethod
    async def oneRec(key: str) -> t.Optional[str]:
        try:
            __fetched = db.Collections.settings_embeds().get_first_list_item(filter=f'key="{key}"')
            return str(__fetched.value)
        except Exception as e:
            logger.error(f"Error: {e}")

    @staticmethod
    async def allVals() -> t.Optional[t.List[Record]]:
        try:
            return db.Collections.settings_embeds().get_full_list()
        except Exception as e:
            logger.error(f"Error: {e}")

    @staticmethod
    async def allErrorVals() -> t.Optional[dict[str, str]]:
        try:
            __fetched = db.Collections.settings_embeds().get_full_list(query_params={"filter": f'key~"ERROR_"'})
            data = {}
            for i in __fetched:
                data[str(i.key)] = str(i.value)
            return data
        except Exception as e:
            logger.error(f"Error: {e}")
    
    @staticmethod
    async def oneThumbnail(key: str) -> t.Optional[str]:
        try:
            __fetched = db.Collections.settings_embeds().get_first_list_item(filter=f'key="thumbnail_{key}"')
            return str(__fetched.value)
        except Exception as e:
            logger.error(f"Error: {e}")
