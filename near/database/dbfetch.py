import typing as t
from loguru import logger
from tortoise.exceptions import DoesNotExist as __DoesNotExist
from .models import (
    DataEmbeds as __DataEmbeds,
    DataAdBroadcast as __DataAdBroadcast,
    DataGeneral as __DataGeneral,
    DataEmbedThumbnails as __DataEmbedThumbnails,
)

class DataEmbedsFetcher:
    @staticmethod
    async def oneRec(key: str) -> t.Optional[__DataEmbeds]:
        try:
            return await __DataEmbeds.get_or_none(key=key)
        except __DoesNotExist:
            logger.error(f"Key: {key} does not exist!")

    @staticmethod
    async def allVals() -> t.Optional[t.List[__DataEmbeds]]:
        return await __DataEmbeds.all()

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
    async def oneVal(key: str) -> t.Optional[__DataEmbedThumbnails]:
        try:
            return await __DataEmbedThumbnails.get_or_none(key=key)
        except __DoesNotExist:
            logger.error(f"Key: {key} does not exist!")
