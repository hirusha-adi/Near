from tortoise import Tortoise, ConfigurationError
from loguru import logger


async def connect_db():
    """Connect to the SQLite database."""
    try:
        await Tortoise.init(
            db_url='sqlite://near/database/dev.db',
            modules={'models': ['near.database.models']}
        )
    except ConfigurationError:
        logger.trace()
        logger.error("Configuration error!")
    logger.info(f"Connected to Tortoise ORM")
    await Tortoise.generate_schemas()
    logger.debug(f"Generated schema.")
