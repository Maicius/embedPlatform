from django.shortcuts import render
from django.http import HttpResponse
from .util.jedis import get_pool
from .util.constant import DISTANCE_KEY,TEMPERATURE_KEY, LIGHT_KEY
import json
import redis
import time

def upload_distance(request):
    distance = request.GET.get('distance')
    print(distance)
    pre_process_data(data=distance, key=DISTANCE_KEY)
    return return_success()

def upload_temperature(request):
    temperature = request.GET.get('temperature')
    pre_process_data(data=temperature, key=TEMPERATURE_KEY)
    return return_success()

def upload_light(request):
    light = request.GET.get('light')
    pre_process_data(light, key=LIGHT_KEY)
    return return_success()

def pre_process_data(data, key):
    now = int(time.time())
    conn = redis.Redis(connection_pool=get_pool())
    distance_dict = dict(time=now, value=data)
    print(key, '===============')
    print(distance_dict)
    conn.rpush(key, str(distance_dict))

def return_success():
    response_data = {'result': '200'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def space(request):
    return render(request, 'show_data.html')

def get_data(request):
    start = request.GET.get('start')
    conn = redis.Redis(connection_pool=get_pool())
    stop = conn.llen(DISTANCE_KEY)

    distance_list = conn.lrange(DISTANCE_KEY, int(start) + 1, stop)

    temperature = conn.lindex(TEMPERATURE_KEY, -1)

    light = conn.lindex(LIGHT_KEY, -1)
    result = {}
    result['distance_list'] = distance_list
    result['start'] = stop
    result['light'] = light
    result['temperature'] = temperature
    return HttpResponse(json.dumps(result), content_type="application/json")