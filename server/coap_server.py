#!/usr/bin/env python3
import datetime
import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
from embed_nju.util.jedis import save_data_to_redis
from embed_nju.util.constant import WET_KEY

class TimeResource(resource.ObservableResource):
    """Example resource that can be observed. The `notify` method keeps
    scheduling itself, and calles `update_state` to trigger sending
    notifications."""

    def __init__(self):
        super().__init__()

        self.handle = None

    def notify(self):
        self.updated_state()
        self.reschedule()

    def reschedule(self):
        self.handle = asyncio.get_event_loop().call_later(5, self.notify)

    def update_observation_count(self, count):
        if count and self.handle is None:
            print("Starting the clock")
            self.reschedule()
        if count == 0 and self.handle:
            print("Stopping the clock")
            self.handle.cancel()
            self.handle = None

    async def render_get(self, request):
        # payload = datetime.datetime.now().\
        #         strftime("%Y-%m-%d %H:%M").encode('ascii')
        # 数据存到redis中
        data=request.payload
        save_data_to_redis(data.decode(encoding='utf-8'),WET_KEY)
        return aiocoap.Message(payload=data)


# logging setup

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)


def start_coap_server():
    # Resource tree creation
    root = resource.Site()

    root.add_resource(('.well-known', 'core'),
                      resource.WKCResource(root.get_resources_as_linkheader))
    root.add_resource(('wet', ), TimeResource())

    asyncio.Task(aiocoap.Context.create_server_context(root))

    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    start_coap_server()