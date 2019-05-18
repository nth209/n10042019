from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponsePermanentRedirect ,HttpRequest
from django.contrib import auth
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.


def setContext():
    conText = {
        'pageTitle' : 'Trang chủ'
    }
    return conText


def index(request):
    context = setContext()
    return render(request, '_1004/index.html', context)


def getTitle(request):
    response = {
        'pageTitle': 'Trang chủ'
    }
    return JsonResponse(response)