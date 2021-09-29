from .response import Response
from .data import Data
from .approve_client import KgbClient


class Flow:
    """Application logic"""

    def __init__(self, recieved_data_from_client: str) -> None:
        self.recv_data = recieved_data_from_client
        self.__response = self.main()
    
    def main(self):
        """Main logic"""
        print('data for kgb', self.recv_data)
        kgb = KgbClient('vragi-vezde.to.digital', 51624)
        kgb.take_recv_data_for_approving(self.recv_data)

        #prop
        if not kgb.is_aproved:
            return Response.not_approved(kgb.get_feedback())
        if kgb.is_bad_request:
            return Response.bad_request()

        data = Data(self.recv_data)
        command = data.get_command()
        name = data.get_name()
        phones = data.get_phones()

        resp = Response(command, name, phones)
        return resp.make_response()

    @property
    def response_for_client(self):
        """Used in server echo handle and return response for client"""
        return self.__response
