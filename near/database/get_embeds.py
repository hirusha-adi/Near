from .db import Embeds

def PleaseWait():
    data = {}
    data["pleasewait_author_name"] = Embeds.get("pleasewait_author_name")
    data["Pleasewait_author_url"] = Embeds.get("Pleasewait_author_url")
    data["pleasewait_color"] = Embeds.get("pleasewait_color")
    data["Pleasewait_description"] = Embeds.get("Pleasewait_description")
    data["pleasewait_footer"] = Embeds.get("pleasewait_footer")
    data["pleasewait_thumbnail"] = Embeds.get("pleasewait_thumbnail")
    data["Pleasewait_title"] = Embeds.get("Pleasewait_title")
    return data

def ErrorEmbeds():
    data = {}
    data["error_color"] = Embeds.get("error_color")
    data["error_description"] = Embeds.get("error_description")
    data["error_feild_name"] = Embeds.get("error_feild_name")
    data["error_thumbnail"] = Embeds.get("error_thumbnail")
    data["error_title"] = Embeds.get("error_title")
    return data

def ErrorEmbeds():
    data = {}
    data["common_color"] = Embeds.get("common_color")
    return data

def FakeEmbeds():
    data = {}
    data["fakeinfo_color"] = Embeds.get("fakeinfo_color")
    data["fakeinfo_thumbnail"] = Embeds.get("fakeinfo_thumbnail")
    data["fakeinfo_title"] = Embeds.get("fakeinfo_title")
    return data
