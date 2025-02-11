import json
import os
from loguru import logger

from . import db


async def set_defaults() -> None:
    """
    Set the default settings for the application by loading data into the
    settings_embeds collection from a predefined JSON configuration file.
    
    This function initializes the database with default values if there are
    no existing records, or updates the database with any new keys found in
    the default configuration that are not already present in the database.
    """
    await __set_defaultsSettingsEmbeds()


async def __set_defaultsSettingsEmbeds() -> None:
    """
    Load the default settings into the settings_embeds collection of the database,
    from file: `near/database/default-data/default.settings_embeds.json`.
    
    - If there is no existing data in the database, all the default settings are loaded.
    - If there is existing data, the function checks if there has been an update in the default config.
      If there is an update, the new added keys are loaded into the database.
    """
    try:
        # from the default config file
        with open(os.path.join("near", "database", "default-data", "default.settings_embeds.json"), "r") as f:
            default_data: dict = json.load(f)
        default_data_keys = [x for x in default_data.keys()]
        
        # form pocketbase
        settings_embeds_all = db.Collections.settings_embeds().get_full_list()
        settings_embeds_all_keys = [x.key for x in settings_embeds_all]
        
        if len(settings_embeds_all_keys) == 0:
            # if no existing data in database
            for key_default, val_default in default_data.items():
                db.Collections.settings_embeds().create(
                    {
                        "key": key_default,
                        "value": val_default
                    }
                )
                logger.debug(f"Added key: {key_default}, value: {val_default}")
            logger.info("Default data loaded into settings_embeds collection.")
            
        elif len(default_data_keys) > len(settings_embeds_all_keys):
            # means there has been an update in the default config
            # in that case, add the new added record only
            # without changing any other thing
            # TODO: BUG: FIX: BROKEN
            #   discord-bot  | 2025-02-11 17:46:16.531 | ERROR    | near.database.defaults:__set_defaultsSettingsEmbeds:69 - Failed to load default data into settings_embeds: cannot access local variable 'val_default' where it is not associated with a value
            missing_keys = set(default_data_keys) - set(settings_embeds_all_keys)
            if missing_keys:
                logger.debug(f"File `default.settings_embeds.json` has been updated! Adding new records.")
                for missing_key in missing_keys:
                    db.Collections.settings_embeds().create(
                        {
                            "key": missing_key,
                            "value": val_default
                        }
                    )
                    logger.debug(f"Added key: {missing_key}, value: {val_default}")
            logger.info("New default data updated into settings_embeds collection.")
                    
    except Exception as e:
        logger.error(f"Failed to load default data into settings_embeds: {e}")
