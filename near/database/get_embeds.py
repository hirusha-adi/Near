import json
import os
import typing as t

__FILENAME = os.path.join(os.getcwd(), 'near', 'database', 'embeds.json')


def _getColor(_code: t.Union[str, bytes], _hex: t.Optional[bool] = False):
    if _hex:
        return False
    else:
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

    def __update(self) -> None:
        with open(__FILENAME, "w", encoding="utf-8") as file:
            self._embed = json.dump(self._embed, file)

    @property
    def TITLE(self):
        return self._embed["PleaseWaitEmbed"]["TITLE"]

    @TITLE.setter
    def TITLE(self, value):
        self._embed["PleaseWaitEmbed"]["TITLE"] = str(value)
        self.__update()

    @property
    def DESCRIPTION(self):
        return self._embed["PleaseWaitEmbed"]["DESCRIPTION"]

    @DESCRIPTION.setter
    def DESCRIPTION(self, value):
        self._embed["PleaseWaitEmbed"]["DESCRIPTION"] = str(value)
        self.__update()

    @property
    def THUMBNAIL(self):
        return self._embed["PleaseWaitEmbed"]["THUMBNAIL"]

    @THUMBNAIL.setter
    def THUMBNAIL(self, value):
        if str(value).lower().startswith('http'):
            self._embed["PleaseWaitEmbed"]["THUMBNAIL"] = str(value)
            self.__update()

    @property
    def FOOTER(self):
        return self._embed["PleaseWaitEmbed"]["FOOTER"]

    @FOOTER.setter
    def FOOTER(self, value):
        self._embed["PleaseWaitEmbed"]["FOOTER"] = str(value)
        self.__update()

    @property
    def COLOR(self):
        return _getColor(self._embed["PleaseWaitEmbed"]["COLOR"])

    @COLOR.setter
    def COLOR(self, value):
        self._embed["PleaseWaitEmbed"]["COLOR"] = _getColor(
            _code=str(value), _hex=True
        )
        self.__update()

    @property
    def AUTHOR_NAME(self):
        return self._embed["PleaseWaitEmbed"]["AUTHOR_NAME"]

    @AUTHOR_NAME.setter
    def AUTHOR_NAME(self, value):
        self._embed["PleaseWaitEmbed"]["AUTHOR_NAME"] = str(value)
        self.__update()

    @property
    def AUTHOR_URL(self):
        return self._embed["PleaseWaitEmbed"]["AUTHOR_URL"]

    @AUTHOR_URL.setter
    def AUTHOR_URL(self, value):
        if str(value).lower().startswith('http'):
            self._embed["PleaseWaitEmbed"]["AUTHOR_URL"] = str(value)
            self.__update()


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
