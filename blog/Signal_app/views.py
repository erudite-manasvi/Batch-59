from django.shortcuts import render
from .signal import custom_signal
from django.http import HttpResponse

# Create your views here.
def trigger_signal(req):
    custom_signal.send(sender=None,user='xyz')
    return HttpResponse('Custome Signal')