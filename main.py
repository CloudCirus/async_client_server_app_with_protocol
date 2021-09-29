import asyncio
from server.server import Server


if __name__ == '__main__':
    """Start server"""
    server = Server('localhost', 3333)
    asyncio.run(server.main())
