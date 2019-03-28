from django.shortcuts import render
from django.http import HttpResponse
from .util.jedis import get_pool, save_data_to_redis
from .util.constant import DISTANCE_KEY,TEMPERATURE_KEY, LIGHT_KEY, WET_KEY
import json
import redis


def upload_distance(request):
    distance = request.GET.get('distance')
    print(distance)
    save_data_to_redis(data=distance, key=DISTANCE_KEY)
    return return_success()

def upload_temperature(request):
    temperature = request.GET.get('temperature')
    save_data_to_redis(data=temperature, key=TEMPERATURE_KEY)
    return return_success()

def upload_light(request):
    light = request.GET.get('light')
    save_data_to_redis(light, key=LIGHT_KEY)
    return return_success()


def return_success():
    response_data = {'result': '200'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def space(request):
    return render(request, 'show_data.html')

def clear_repeat(data):
    key_set = set()
    for item in data:
        item = json.loads(item)
        if item['time'] in key_set:
            data.remove(item)
        else:
            key_set.add(item['time'])
    return data

def get_data(request):
    """
    响应前端
    :param request:
    :return:
    """
    start = request.GET.get('start')
    conn = redis.Redis(connection_pool=get_pool())
    stop = conn.llen(DISTANCE_KEY)

    try:
        distance_list = conn.lrange(DISTANCE_KEY, int(start), stop)
        distance_list = clear_repeat(distance_list)
    except BaseException as e:
        raise e
        distance_list = []

    temperature = conn.lindex(TEMPERATURE_KEY, -1)
    if temperature:
        temperature = json.loads(temperature)
    light = conn.lindex(LIGHT_KEY, -1)

    wet = conn.lindex(WET_KEY, -1)
    if wet:
        wet = json.loads(wet)
    if light:
        light = json.loads(light)
    result = {}
    result['distance_list'] = distance_list
    result['start'] = stop
    result['light'] = light
    result['temperature'] = temperature
    result['wet'] = wet
    return HttpResponse(json.dumps(result), content_type="application/json")