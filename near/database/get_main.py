import json
import os
import typing as t


class BotMainDB:
    """
    Main settings of the bot
    loaded from 
        near/database/main.json

    `MESSAGE_PREFIX` (str):
        the bot prefix

    `BOT_CREATOR_NAME` (str):
        the name of the creator of the discord bot

    `BOT_VERSION` (str):
        the version of the bot

    `DEV_ID` (int):
        ID of the main developer

    `DEV_AND_OWNERS` (list):
        a list of users able to manage the bot
    """

    def __init__(self) -> None:
        self._main_json = os.path.join(
            os.getcwd(), 'near', 'database', 'main.json'
        )
        with open(self._main_json, "r", encoding="utf-8") as file:
            self._embed = json.load(file)

    def __update(self):
        with open(self._main_json, "w", encoding="utf-8") as file:
            self._embed = json.dump(self._embed, file)

    @property
    def MESSAGE_PREFIX(self):
        return self._embed["MESSAGE_PREFIX"]

    @MESSAGE_PREFIX.setter
    def MESSAGE_PREFIX(self, value: t.Any):
        """Bot prefix must be less than 8 characters long or equal to 8"""
        if not(len(value) >= 8):
            value = str(value)
        else:
            value = "."
        self._embed["MESSAGE_PREFIX"] = value
        self.__update()

    @property
    def BOT_CREATOR_NAME(self):
        return self._embed["BOT_CREATOR_NAME"]

    @BOT_CREATOR_NAME.setter
    def BOT_CREATOR_NAME(self, value: t.Any):
        self._embed["BOT_CREATOR_NAME"] = str(value)
        self.__update()

    @property
    def BOT_VERSION(self):
        return self._embed["BOT_VERSION"]

    @BOT_VERSION.setter
    def BOT_VERSION(self, value: t.Any):
        value = str(value)
        if value.lower().startswith('v'):
            final = value
        else:
            final = 'v' + value
        self._embed["BOT_VERSION"] = final
        self.__update()

    @property
    def DEV_ID(self):
        return self._embed["DEV_ID"]

    @DEV_ID.setter
    def DEV_ID(self, value: t.Any):
        # will raise ValueError by default if not proper int
        self._embed["DEV_ID"] = int(value)
        self.__update()

    @property
    def DEV_AND_OWNERS(self):
        return self._embed["DEV_AND_OWNERS"]

    @DEV_AND_OWNERS.setter
    def DEV_AND_OWNERS(self, value: t.Any):
        if "," in str(value):
            values = str(value).split(',')
            for i in values:
                try:
                    self._embed["DEV_AND_OWNERS"].append(int(values))
                except ValueError:
                    continue
        else:
            try:
                self._embed["DEV_AND_OWNERS"].append(int(value))
            except ValueError:
                pass
        self.__update()
