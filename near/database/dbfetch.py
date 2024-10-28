import typing as t
from loguru import logger
from tortoise.exceptions import DoesNotExist
from .models import DataEmbeds, DataAdBroadcast, DataGeneral


class FetchAll:
    @staticmethod
    async def fetch_embeds() -> list[DataEmbeds]:
        try:
            return await DataEmbeds.all()
        except DoesNotExist:
            logger.error("Key: ")
            
class DataEmbedsFetcher:
    @staticmethod
    async def one(key: str) -> t.Optional[DataEmbeds]:
        try:
            return await DataEmbeds.get_or_none(key=key)
        except DoesNotExist:
            logger.error(f"Key: {key} does not exist!")

    @staticmethod
    async def all() -> t.Optional[t.List[DataEmbeds]]:
        return await DataEmbeds.all()
