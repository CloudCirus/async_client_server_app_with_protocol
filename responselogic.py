from enum import Enum
from fileslogic import FilesLogic
from typing import Union
from settings import PROTOCOL
from requestslogic import Request


class ResponseStatus(Enum):
    """Response statuses specified in RKSOK specs for responses"""
    OK = "НОРМАЛДЫКС"
    NOTFOUND = "НИНАШОЛ"
    NOT_APPROVED = "НИЛЬЗЯ"
    INCORRECT_REQUEST = "НИПОНЯЛ"


RESP = ResponseStatus
ENDING = '\r\n\r\n'


class Response(Request):
    """Make responses and handle data for them"""

    def __init__(self, command: str, name: str, phones: Union[str, None]) -> None:
        self.command = command
        self.name = name
        self.phones = phones

    def ok_resp(self, phones) -> str:
        if phones:
            return f'{RESP.OK.value} {PROTOCOL}\r\n{phones}{ENDING}'
        else:
            return f'{RESP.OK.value} {PROTOCOL}{ENDING}'

    def not_found_resp(self) -> str:
        return f'{RESP.NOTFOUND.value} {PROTOCOL}{ENDING}'

    def not_approved(self, body) -> str:
        return f'{RESP.NOT_APPROVED.value} {PROTOCOL}\r\n{body}{ENDING}'

    def bad_request(self) -> str:
        return f'{RESP.INCORRECT_REQUEST.value} {PROTOCOL}{ENDING}'

    def make_response(self) -> str:
        """used in mail logic for make response and handle data"""
        files = FilesLogic(self.name, self.phones)
        phones = None
        print('\n')
        if self.get_command():
            phones = files.get_phones()
            if not phones:
                return self.not_found_resp()
        if self.write_command():
            files.write_file()
        if self.delete_command():
            files.delete_file()
        return self.ok_resp(phones)
