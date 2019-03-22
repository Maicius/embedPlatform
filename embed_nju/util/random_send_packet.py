import requests
import multiprocessing
import random
import json
from time import sleep

def send_distance():
    i = 0
    headers = {
        'content-type': 'application/json'
    }
    while i < 100:
        distance = random.randint(1, 100)
        requests.get(url='http://127.0.0.1:8000/upload_distance?distance=' + str(distance), headers=headers)
        i += 1
        print(distance)
        sleep(1)


def send_temperature():
    i = 0
    while i < 100:
        distance = random.randint(1, 100)
        requests.get(url='http://127.0.0.1:8000/upload_temperature?temperature=' + str(distance))
        i += 1
        sleep(5)

def send_light():
    i = 0
    while i < 100:
        distance = random.randint(1, 100)
        requests.get(url='http://127.0.0.1:8000/upload_temperature?light=' + str(distance))
        i += 1
        sleep(10)

if __name__ == '__main__':
    dis = multiprocessing.Process(target=send_distance)
    dis.daemon = True
    # temp = multiprocessing.Process(target=send_temperature)
    # temp.daemon = True
    # light = multiprocessing.Process(target=send_light)
    # light.daemon = True

    dis.start()
    dis.join()
    # temp.start()
    # light.start()
    #
    #
    # temp.join()
    # light.join()
