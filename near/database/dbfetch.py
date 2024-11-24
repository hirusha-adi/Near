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
        """
        Fetches a single embed record from the 'settings_embeds' collection.

        Parameters
        ----------
        key : str
            The key of the embed record to fetch.

        Returns:
        -------
        t.Optional[str]
            The value of the record if found, None otherwise.
        """
        try:
            __fetched = db.Collections.settings_embeds().get_first_list_item(filter=f'key="{key}"')
            return str(__fetched.value)
        except Exception as e:
            logger.error(f"Error: {e}")

    @staticmethod
    async def allVals() -> t.Optional[t.List[Record]]:
        """
        Fetches all records from the 'settings_embeds' collection.

        Returns:
        -------
        t.Optional[t.List[Record]]
            A list of all records in the collection 
            if successful, None otherwise.
        """
        try:
            return db.Collections.settings_embeds().get_full_list()
        except Exception as e:
            logger.error(f"Error: {e}")

    @staticmethod
    async def allErrorVals() -> t.Optional[dict[str, str]]:
        """
        Fetches all records from the 'settings_embeds' collection whose key starts with 'ERROR_'

        Returns:
        -------
        t.Optional[dict[str, str]]
            A dictionary of all records in the collection 
            if successful, None otherwise.
        """
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
        """
        Fetches the value of the thumbnail with the given key from the 'settings_embeds' collection.

        Parameters
        ----------
        key : str
            The key of the thumbnail to fetch (without the 'thumbnail_' prefix).

        Returns
        -------
        t.Optional[str]
            The value of the thumbnail with the given key if successful, None otherwise.
        """
        try:
            __fetched = db.Collections.settings_embeds().get_first_list_item(filter=f'key="thumbnail_{key}"')
            return str(__fetched.value)
        except Exception as e:
            logger.error(f"Error: {e}")
