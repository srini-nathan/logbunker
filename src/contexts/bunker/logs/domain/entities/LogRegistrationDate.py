from datetime import datetime

from src.contexts.shared.domain.valueobj.ValueObject import ValueObject


class LogRegistrationDate(ValueObject):

    def __init__(self, value: datetime):
        super().__init__(value)
