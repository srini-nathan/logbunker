from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class LogNotFoundError(DomainError):

    ERROR_ID = 'a312db5c-f566-4632-8b03-c1c16725c121'

    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'Log not found.'
        self.message = msg

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'message': self.message,
            'id': self.ERROR_ID,
        }

    def get_id(self) -> str:
        return self.ERROR_ID
