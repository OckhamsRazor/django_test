import json
import time
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def index(request):
    page = {
        'title': 'Measure Clock Skew',
    }

    context = {
        'page': page,
    }

    return render(request, 'clock_skew/index.html', context)

def time_stamp(request):
    return HttpResponse(json.dumps({
        'time': 1000*time.time(),
    }), mimetype='application/json')
