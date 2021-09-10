import asyncio
import time
from settings import ENCODING
from asyncio import StreamReader, StreamWriter
from logic import Logic


class Server:
    """Server that answering on client requests with protocol"""

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    async def handle_echo(self, reader: StreamReader, writer: StreamWriter):
        """Collect recieved data from client, handle the logic
        and send back the response"""
        print(f'start handle...\n')
        client_recv_data = str()
        while True:
            client_recv_data_bytes = await reader.read(1024)
            print('take recieved data...\n')
            client_recv_data += client_recv_data_bytes.decode(ENCODING)
            if client_recv_data.endswith('\r\n\r\n'):
                break
            if not client_recv_data_bytes:
                break
            else:
                time.sleep(10)
                break

        addr = writer.get_extra_info('peername')
        print(f'received:\n{client_recv_data!r}\nfrom\n{addr!r}')

        logic = Logic(client_recv_data)
        response = logic.response_for_client()

        writer.write(response.encode(ENCODING))
        print(f'send:\n{response!r}')
        await writer.drain()

        writer.close()
        print('\nclose the connection...')

    async def main(self) -> None:
        """Create server"""
        server = await asyncio.start_server(
            self.handle_echo, self.host, self.port)

        addr = server.sockets[0].getsockname()
        print(f'serving on {addr}')

        async with server:
            await server.serve_forever()
