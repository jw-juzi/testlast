from django.urls import path

from testredis import views

urlpatterns = [
    path('index/', views.index),

    path('testCache/', views.testCache)
]
