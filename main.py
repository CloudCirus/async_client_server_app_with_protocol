import asyncio
from server.server import Server


if __name__ == '__main__':
    """Start server"""
    server = Server('0.0.0.0', 51666)
    asyncio.run(server.main())
