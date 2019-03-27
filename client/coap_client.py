import logging
import asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)

async def main():
    protocol = await Context.create_client_context()
    payload=b"darkness:1000;distance:3"
    request = Message(code=GET, payload=payload, uri='coap://localhost/time')

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r'%(response.code, response.payload))

def start_coap_client():
    asyncio.get_event_loop().run_until_complete(main())

if __name__ == "__main__":
    start_coap_client()