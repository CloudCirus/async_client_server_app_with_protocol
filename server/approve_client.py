import socket
from random import randint
from .settings import ENCODING, Convertor
from .requests import Request
from .response import ResponseStatus as RS


class KgbClient:
    """Client for approving requests to server"""

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.status = None
        self.client_recv_data = None
        self.feedback = None
        self.response = str()
        self.bad_status = RS.INCORRECT_REQUEST.value
        self.not_approve = RS.NOT_APPROVED.value

    def ask_kgb(self) -> str:
        """Use recieved data from client, send it for approving server and collect response"""
        kgb = socket.create_connection((self.host, self.port))
        print('self kgb data:', self.client_recv_data)

        kgb_request = Request.kgb_request(self.client_recv_data)
        print('approving...', kgb_request, sep='\n')
        kgb.send(Convertor.str_to_bytes(kgb_request))
        resp = str()
        while True:
            data = Convertor.bytes_to_str(kgb.recv(1024))
            resp += data
            if resp.endswith('\r\n\r\n'):
                break
            if not data:
                break
            else:
                kgb.settimeout(5)
                print('break with timeout!')
                break
        print('answer_from_kgb:',
              f'хер_майор №{randint(1, 666)}: {resp}', sep='\n')
        self.response = resp

    def take_recv_data_for_approving(self, recv_data: str):
        """Collect client request for approving client"""
        self.client_recv_data = recv_data
        self.ask_kgb()
        self.get_status()

    def get_status(self) -> str:
        """Collect response status from approving server"""
        self.status = self.response.split()[0]

    def get_feedback(self) -> str:
        """Collect response feedback massage from approving server"""
        self.feedback = self.response.split('\r\n')[1]

    @property
    def is_aproved(self) -> bool:
        """Checks if response status is not approved"""
        return self.not_approve != self.status

    @property
    def is_bad_request(self):
        """Checks if response status means that client request was bad"""
        return self.bad_status == self.status
