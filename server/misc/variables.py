import asyncio

from server.utils.types import Client

clients: dict[asyncio.StreamWriter, Client] = {}
bans: set[str] = set()
