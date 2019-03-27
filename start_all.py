from server.xmpp_server import start_xmpp_server
from server.coap_server import start_coap_server
from server.mqtt_subscribe import start_mqtt_server
from server.http_server import start_http_server
from client.coap_client import start_coap_client
from client.http_client import start_http_client
from client.mqtt_client import start_mqtt_client
from client.read_serial import read_serial

import multiprocessing

"""
start all servers and clients
"""

if __name__ == '__main__':

    http_server = multiprocessing.Process(target=start_http_server)
    http_server.daemon = True

    http_client = multiprocessing.Process(target=start_http_client)
    http_client.daemon = True

    mqtt_client = multiprocessing.Process(target=start_mqtt_client)
    mqtt_client.daemon = True

    coap_client = multiprocessing.Process(target=start_coap_client)
    coap_client.daemon = True

    read_serial = multiprocessing.Process(target=read_serial)
    read_serial.daemon = True

    # TODO XMPP CLIENT

    coap_server = multiprocessing.Process(target=start_coap_server)
    coap_server.daemon = True

    xmpp_server = multiprocessing.Process(target=start_xmpp_server)
    xmpp_server.daemon = True

    mqtt_server = multiprocessing.Process(target=start_mqtt_server)
    mqtt_server.daemon = True


    read_serial.start()

    http_server.start()
    http_client.start()
    mqtt_client.start()
    coap_client.start()

    coap_server.start()
    xmpp_server.start()
    mqtt_server.start()

    read_serial.join()
    http_server.join()
    http_client.join()
    mqtt_client.join()
    coap_client.join()

    coap_server.join()
    xmpp_server.join()
    mqtt_server.join()