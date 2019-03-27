import logging
import asyncio

from aiocoap import *
from embed_nju.util.jedis import pop_raw_data
from embed_nju.util.constant import RAW_WET_KEY

logging.basicConfig(level=logging.INFO)

async def main():
    protocol = await Context.create_client_context()
    payload=pop_raw_data(RAW_WET_KEY)
    request = Message(code='GET', payload=payload.encode(encoding='utf-8'), uri='coap://localhost/wet')

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
    while True:
        start_coap_client()