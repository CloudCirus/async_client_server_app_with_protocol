from responselogic import ResponseLogic
from data import Data
from approveclient import KgbClient


class Logic:
    """Encapsulates the application logic"""

    def __init__(self, recieved_data_from_client: str) -> None:
        self.recv_data = recieved_data_from_client
        self.response = self.__main()

    def __main(self):
        """Encapsulates main logic"""
        print('data for kgb', self.recv_data)
        kgb = KgbClient('vragi-vezde.to.digital', 51624)
        kgb.take_recv_data_for_approving(self.recv_data)

        if kgb.is_not_ok():
            return ResponseLogic.not_approved(kgb.get_feedback())
        if kgb.is_bad_request():
            return ResponseLogic.bad_request()

        data = Data(self.recv_data)
        command = data.get_command()
        name = data.get_name()
        phones = data.get_phones()

        resp = ResponseLogic(command, name, phones)
        return resp.make_response()

    def response_for_client(self):
        """Used in server echo handle and return response for client"""
        return self.response
