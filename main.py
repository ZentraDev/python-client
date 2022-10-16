#!/usr/bin/env python

import asyncio
import logging
from pprint import pprint

from zentra import Client, Message

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("httpx").setLevel(logging.INFO)
logging.getLogger("asyncio").setLevel(logging.INFO)
logging.getLogger("websockets").setLevel(logging.INFO)


async def print_new_message(message: Message):
    print(f"{message.sender_name} said: '{message.content}'")


async def main():
    client: Client = Client("Skelmis", call_on_message=print_new_message)
    await client.connect()

    await client.send_message(content="world", conversation_id=4)

    # Run forever
    await asyncio.Future()


asyncio.run(main())
