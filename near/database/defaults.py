import json
import os
from . import db

async def set_defaults():
    await __set_defaultsSettingsEmbeds()


async def __set_defaultsSettingsEmbeds():
    settings_embeds_all = db.Collections.settings_embeds().get_full_list()
    settings_embeds_all_keys = [x.key for x in settings_embeds_all]
    if len(settings_embeds_all_keys) == 0:
        try:
            with open(os.path.join("near", "database", "default-data", "default.settings_embeds.json"), "r") as f:
                default_data: dict = json.load(f)
            # -------------------------------------
            for key_default, val_default in default_data.items():
                db.Collections.settings_embeds().create(
                    {
                        "key": key_default,
                        "value": val_default
                    }
                )
            # -------------------------------------
            print("Default data loaded into DataEmbeds table.")
        except Exception as e:
            print(f"Failed to load default data into DataEmbeds: {e}")
