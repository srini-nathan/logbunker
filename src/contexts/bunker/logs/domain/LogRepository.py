from abc import ABC
from typing import NoReturn

from src.contexts.bunker.logs.domain.entities.Log import Log


class LogRepository(ABC):

    async def create_one(self, log: Log) -> NoReturn:
        raise NotImplementedError()
