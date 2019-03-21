from django.shortcuts import render
import random
from django.http import HttpResponse

import json
import hashlib
from django.http import HttpResponseRedirect

def upload_data(request):
    data = request.GET.get('data')
    print(data)
    return_success()

def return_success():

    response_data = {'result': '200'}
    print(response_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")