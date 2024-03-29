from datetime import datetime
from typing import Dict, List, Union, Any

from src.contexts.bunker.logs.domain.domainevents.LogCreatedDomainEvent import LogCreatedDomainEvent
from src.contexts.bunker.logs.domain.entities.LogContent import LogContent
from src.contexts.bunker.logs.domain.entities.LogCreationDate import LogCreationDate
from src.contexts.bunker.logs.domain.entities.LogId import LogId
from src.contexts.bunker.logs.domain.entities.LogLevel import LogLevel
from src.contexts.bunker.logs.domain.entities.LogOrigin import LogOrigin
from src.contexts.bunker.logs.domain.entities.LogRegistrationDate import LogRegistrationDate
from src.contexts.bunker.logs.domain.entities.LogTrace import LogTrace
from src.contexts.bunker.logs.domain.entities.LogType import LogType
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class Log(AggregateRoot):

    def __init__(
            self,
            log_id: LogId,
            content: LogContent,
            level: LogLevel,
            origin: LogOrigin,
            log_type: LogType,
            trace: LogTrace,
            creation_date: LogCreationDate,
            registration_date: LogRegistrationDate = None,
    ):
        super().__init__()
        self.id = log_id
        self.content = content
        self.level = level
        self.origin = origin
        self.type = log_type
        self.trace = trace
        self.creation_date = creation_date
        if registration_date is None:
            registration_date = LogRegistrationDate(datetime.now())
        self.registration_date = registration_date

    @staticmethod
    def create(
            log_id: LogId,
            content: LogContent,
            level: LogLevel,
            origin: LogOrigin,
            log_type: LogType,
            trace: LogTrace,
            creation_date: LogCreationDate,
    ):
        log = Log(log_id, content, level, origin, log_type, trace, creation_date)
        event = LogCreatedDomainEvent(
            log.id.value(),
            log.content.value(),
            log.level.value(),
            log.origin.value(),
            log.type.value(),
            log.trace.value(),
            log.creation_date.value(),
            log.registration_date.value(),
        )
        log.record_event(event)
        return log

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        log = Log(
            LogId(raw_data.get('id')),
            LogContent(raw_data.get('content')),
            LogLevel(raw_data.get('level')),
            LogOrigin(raw_data.get('origin')),
            LogType(raw_data.get('type')),
            LogTrace(raw_data.get('trace')),
            LogCreationDate(raw_data.get('creation-date')),
            LogRegistrationDate(raw_data.get('registration-date')),
        )
        return log

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'id': self.id.value(),
            'content': self.content.value(),
            'level': self.level.value(),
            'origin': self.origin.value(),
            'type': self.type.value(),
            'trace': self.trace.value(),
            'creation-date': self.creation_date.value(),
            'registration-date': self.registration_date.value(),
        }
