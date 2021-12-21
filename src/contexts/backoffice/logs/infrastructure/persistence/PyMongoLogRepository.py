from typing import NoReturn

from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError

from src.contexts.backoffice.logs.domain.LogRepository import LogRepository
from src.contexts.backoffice.logs.domain.entities.Log import Log
from src.contexts.backoffice.logs.domain.errors.LogAlreadyExistsError import LogAlreadyExistsError
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoRepository import PyMongoRepository


class PyMongoLogRepository(PyMongoRepository, LogRepository):

    __COLLECTION_NAME = 'logs'
    __DATABASE_NAME = 'logbunker'

    def __init__(self, client: MongoClient):
        super().__init__(client)
        super()._get_collection().create_index([
            ('id', ASCENDING)
        ], unique=True)

    def get_database_name(self):
        return self.__DATABASE_NAME

    def get_collection_name(self):
        return self.__COLLECTION_NAME

    async def create_one(self, log: Log) -> NoReturn:
        try:
            await super()._create_one(log.to_primitives())
        except DuplicateKeyError as e:
            raise LogAlreadyExistsError('Log with ID <{}> already exists.'.format(log.id.value()))