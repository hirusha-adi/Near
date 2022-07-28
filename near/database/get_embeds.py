import json
import os
import typing as t

__FILENAME = os.path.join(os.getcwd(), 'near', 'database', 'embeds.json')


def _getColor(_code):
    if _code == "red":
        ret = 0xff0000
    elif _code == "green":
        ret = 0x00ff00
    elif _code == "blue":
        ret = 0x0000ff
    return ret


class PleaseWait:

    def __init__(self) -> None:
        with open(__FILENAME, "r", encoding="utf-8") as file:
            self._embed = json.load(file)

    @property
    def TITLE(self):
        return self._embed["PleaseWaitEmbed"]["TITLE"]

    @property
    def DESCRIPTION(self):
        return self._embed["PleaseWaitEmbed"]["DESCRIPTION"]

    @property
    def THUMBNAIL(self):
        return self.embed["PleaseWaitEmbed"]["THUMBNAIL"]

    @property
    def FOOTER(self):
        return self._embed["PleaseWaitEmbed"]["FOOTER"]

    @property
    def COLOR(self):
        return _getColor(self._embed["PleaseWaitEmbed"]["COLOR"])

    @property
    def AUTHOR_NAME(self):
        return self._embed["PleaseWaitEmbed"]["AUTHOR_NAME"]

    @property
    def AUTHOR_URL(self):
        return self._embed["PleaseWaitEmbed"]["AUTHOR_URL"]


class ErrorEmbeds:
    def __init__(self) -> None:
        with open(__FILENAME, "r", encoding="utf-8") as file:
            self._embed = json.load(file)

    @property
    def TITLE(self):
        return self._embed["ERROR"]["TITLE"]

    @property
    def DESCRIPTION(self):
        return self._embed["ERROR"]["DESCRIPTION"]

    @property
    def THUMBNAIL(self):
        return self._embed["ERROR"]["THUMBNAIL"]

    @property
    def FIELD_NAME(self):
        return self._embed["ERROR"]["FIELD_NAME"]

    @property
    def COLOR(self):
        return _getColor(self._embed["ERROR"]["COLOR"])


class Common:
    def __init__(self) -> None:
        with open(__FILENAME, "r", encoding="utf-8") as file:
            self._embed = json.load(file)

    @property
    def COLOR(self):
        return _getColor(self._embed["COMMON"]["COLOR"])


class FakeEmbeds:
    def __init__(self) -> None:
        with open(__FILENAME, "r", encoding="utf-8") as file:
            self._embed = json.load(file)

    @property
    def TITLE(self):
        return self._embed["FAKEEMBEDS"]["TITLE"]

    @property
    def THUMBNAIL(self):
        return self._embed["FAKEEMBEDS"]["THUMBNAIL"]
    
    @property
    def COLOR(self):
        return _getColor(self._embed["FAKEEMBEDS"]["COLOR"])
