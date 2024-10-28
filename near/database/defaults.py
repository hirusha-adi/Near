from .models import DataAdBroadcast, DataEmbeds, DataGeneral
from tortoise.transactions import in_transaction
import json, os

async def set_defaults():
    await __set_defaultsDataEmbeds()

async def __set_defaultsDataEmbeds():
    if await DataEmbeds.all().count() == 0:
        try:
            with open(os.path.join("near", "database", "default-data", "default.dataembeds.json"), "r") as f:
                default_data = json.load(f)
            # -------------------------------------
            async with in_transaction():
                # PleaseWaitEmbed
                await DataEmbeds.create(key="PleaseWaitEmbed_AUTHOR_NAME", value=default_data["PleaseWaitEmbed"]["AUTHOR_NAME"])
                await DataEmbeds.create(key="PleaseWaitEmbed_AUTHOR_URL", value=default_data["PleaseWaitEmbed"]["AUTHOR_URL"])
                await DataEmbeds.create(key="PleaseWaitEmbed_TITLE", value=default_data["PleaseWaitEmbed"]["TITLE"])
                await DataEmbeds.create(key="PleaseWaitEmbed_DESCRIPTION", value=default_data["PleaseWaitEmbed"]["DESCRIPTION"])
                await DataEmbeds.create(key="PleaseWaitEmbed_COLOR", value=default_data["PleaseWaitEmbed"]["COLOR"])
                await DataEmbeds.create(key="PleaseWaitEmbed_THUMBNAIL", value=default_data["PleaseWaitEmbed"]["THUMBNAIL"])
                await DataEmbeds.create(key="PleaseWaitEmbed_FOOTER", value=default_data["PleaseWaitEmbed"]["FOOTER"])
                # ERROR
                await DataEmbeds.create(key="ERROR_TITLE", value=default_data["ERROR"]["TITLE"])
                await DataEmbeds.create(key="ERROR_DESCRIPTION", value=default_data["ERROR"]["DESCRIPTION"])
                await DataEmbeds.create(key="ERROR_THUMBNAIL", value=default_data["ERROR"]["THUMBNAIL"])
                await DataEmbeds.create(key="ERROR_FIELD_NAME", value=default_data["ERROR"]["FIELD_NAME"])
                await DataEmbeds.create(key="ERROR_COLOR", value=default_data["ERROR"]["COLOR"])
                # COMMON
                await DataEmbeds.create(key="COMMON_COLOR", value=default_data["COMMON"]["COLOR"])
                # FAKEEMBEDS
                await DataEmbeds.create(key="FAKEEMBEDS_THUMBNAIL", value=default_data["FAKEEMBEDS"]["THUMBNAIL"])
                await DataEmbeds.create(key="FAKEEMBEDS_COLOR", value=default_data["FAKEEMBEDS"]["COLOR"])
                await DataEmbeds.create(key="FAKEEMBEDS_TITLE", value=default_data["FAKEEMBEDS"]["TITLE"])
            # -------------------------------------
            print("Default data loaded into DataEmbeds table.")
        except Exception as e:
            print(f"Failed to load default data into DataEmbeds: {e}")
    