import time
from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource
from embed_nju.util.jedis import save_data_to_redis
from embed_nju.util.constant import WET_KEY

class BasicResource(Resource):
    def __init__(self, name="BasicResource", coap_server=None):
        super(BasicResource, self).__init__(
            name,
            coap_server,
            visible=True,
            observable=True,
            allow_children=True)
        self.payload = "Basic Resource"
        self.resource_type = "rt1"
        self.content_type = "text/plain"
        self.interface_type = "if1"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.edit_resource(request)
        return self

    def render_POST(self, request):
        res = self.init_resource(request, BasicResource())
        # print('========================================')
        data=request.payload
        save_data_to_redis(data,WET_KEY)
        # print(request.payload)
        return res

    def render_DELETE(self, request):
        return True


class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('wet/', BasicResource())


def start_coap_server():
    server = CoAPServer("0.0.0.0", 5683)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")


if __name__ == '__main__':
    start_coap_server()
