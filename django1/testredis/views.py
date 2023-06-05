from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return HttpResponse('index')


def testCache(request):
    redis_value = cache.get('ip')
    if redis_value:
        print(redis_value)
        return HttpResponse('缓存数据')
    else:
        ip = request.META.get('REMOTE_ADDR')
        cache.set('ip', ip)
        cache.expire('ip', 60)
        return HttpResponse('缓存没有数据')
