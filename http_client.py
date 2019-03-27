import serial
import requests
from time import sleep

def send_packet_by_http(data):
    data = data.split(':')
    data_type = data[0]
    data_value = data[1]

    url = 'http://localhost:8000/'
    if data_type == 'temperature':
        url = url + 'upload_temperature?' + data_type + '=' + data_value
    elif data_type == 'distance':
        url = url + 'upload_distance?' + data_type + '=' + data_value
    elif data_type == 'light':
        url = url + 'upload_light?' + data_type + '=' + data_value

    print(url)
    requests.get(url)

def read_serial():
    with serial.Serial('/dev/tty', 9600) as ser:
        while True:
            data = ser.readline().decode()
            send_packet_by_http(data)

def send_simulate():
    while True:
        data = 'temperature:10'
        send_packet_by_http(data)
        data = 'distance:10'
        send_packet_by_http(data)
        data = 'light:10'
        send_packet_by_http(data)
        sleep(1)

if __name__ == '__main__':
    send_simulate()