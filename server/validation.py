from server.data import Data
from .settings import Convertor
from .response import Response
from .requests import RequestCommand


class Validator:
    def __init__(self, recv_data: bytes) -> None:
        self.recv_data = recv_data
        self.finish_data = None

    def validation(self):
        string = Convertor.bytes_to_str(self.recv_data)
        data_list = Data(string)
        command = data_list.get_command()
        # name = data_list.get_name()
        if len(data_list) > 2:
            phone = data_list.get_phones()
        for el in RequestCommand:
            if command == el.value:
                break
            else:
                return self.finish_data
        if phone:
            if not phone.isdigit():
                return self.finish_data
        return string
        
