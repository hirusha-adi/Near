import typing as t
from loguru import logger
from tortoise.exceptions import DoesNotExist
from .models import DataEmbeds, DataAdBroadcast, DataGeneral


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

    @staticmethod
    async def allError() -> t.Optional[dict]:
        all_ = await DataEmbedsFetcher.all()
        data = {}
        for i in all_:
            if i.key.startswith("ERROR_"):
                data[i.key] = i.value
        return data
