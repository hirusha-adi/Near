import typing as t
from loguru import logger
from tortoise.exceptions import DoesNotExist
from .models import DataEmbeds, DataAdBroadcast, DataGeneral, DataEmbedThumbnails


class DataEmbedsFetcher:
    @staticmethod
    async def oneRec(key: str) -> t.Optional[str]:
        try:
            __fetched = await DataEmbeds.get(key=key)
            return __fetched.value
        except DoesNotExist:
            logger.error(f"Key: {key} does not exist!")

    @staticmethod
    async def allVals() -> t.Optional[t.List[DataEmbeds]]:
        return await DataEmbeds.all()

    @staticmethod
    async def allErrorVals() -> t.Optional[dict]:
        all_ = await DataEmbedsFetcher.allVals()
        data = {}
        for i in all_:
            if i.key.startswith("ERROR_"):
                data[i.key] = i.value
        return data


class DataEmbedThumbnailsFetcher:
    @staticmethod
    async def oneVal(key: str) -> t.Optional[str]:
        try:
            __fetched = await DataEmbedThumbnails.get(key=key)
            return __fetched.value
        except DoesNotExist:
            logger.error(f"Key: {key} does not exist!")
