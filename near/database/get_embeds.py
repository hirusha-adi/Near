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
    with open(__FILENAME, "r", encoding="utf-8") as file:
        embed = json.load(file)

    TITLE = embed["PleaseWaitEmbed"]["TITLE"]
    DESCRIPTION = embed["PleaseWaitEmbed"]["DESCRIPTION"]
    THUMBNAIL = embed["PleaseWaitEmbed"]["THUMBNAIL"]
    FOOTER = embed["PleaseWaitEmbed"]["FOOTER"]
    COLOR = _getColor(embed["PleaseWaitEmbed"]["COLOR"])
    AUTHOR_NAME = embed["PleaseWaitEmbed"]["AUTHOR_NAME"]
    AUTHOR_URL = embed["PleaseWaitEmbed"]["AUTHOR_URL"]


class ErrorEmbeds:
    with open(__FILENAME, "r", encoding="utf-8") as file:
        embed = json.load(file)

    TITLE = embed["ERROR"]["TITLE"]
    DESCRIPTION = embed["ERROR"]["DESCRIPTION"]
    THUMBNAIL = embed["ERROR"]["THUMBNAIL"]
    FIELD_NAME = embed["ERROR"]["FIELD_NAME"]
    COLOR = _getColor(embed["ERROR"]["COLOR"])


class Common:
    with open(__FILENAME, "r", encoding="utf-8") as file:
        embed = json.load(file)

    COLOR = _getColor(embed["COMMON"]["COLOR"])


class FakeEmbeds:
    with open(__FILENAME, "r", encoding="utf-8") as file:
        embed = json.load(file)

    TITLE = embed["FAKEEMBEDS"]["TITLE"]
    THUMBNAIL = embed["FAKEEMBEDS"]["THUMBNAIL"]
    COLOR = _getColor(embed["FAKEEMBEDS"]["COLOR"])
