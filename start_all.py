from server.xmpp_server import start_xmpp_server
from server.coap_server import start_coap_server
from server.mqtt_subscribe import start_mqtt_server

from client.coap_client import start_coap_client
from client.http_client import start_http_client
from client.mqtt_client import start_mqtt_client


# 启动客户端
# start_coap_client()
start_http_client()
start_mqtt_client()

# 启动服务器
start_coap_server()
start_xmpp_server()
start_mqtt_server()