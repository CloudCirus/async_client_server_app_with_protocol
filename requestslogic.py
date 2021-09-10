from enum import Enum
from settings import PROTOCOL


class RequestCommand(Enum):
    """Commands specified in RKSOK specs for requests"""
    GET = "ОТДОВАЙ"
    DELETE = "УДОЛИ"
    WRITE = "ЗОПИШИ"
    APPROVE = "АМОЖНА?"


class RequestLogic:
    """Simplifies request processing"""

    def __init__(self, command: str) -> None:
        self.command = command

    def get_command(self) -> bool:
        if self.command == RequestCommand.GET.value:
            return True
        else:
            False

    def write_command(self) -> bool:
        if self.command == RequestCommand.WRITE.value:
            return True
        else:
            False

    def delete_command(self) -> bool:
        if self.command == RequestCommand.DELETE.value:
            return True
        else:
            False

    def kgb_request(data: str) -> str:
        """Make request for approving server"""
        return f'{RequestCommand.APPROVE.value} {PROTOCOL}\n{data}'
