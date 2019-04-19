from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^DevIdInterface$', views.DevIdInterface),
    url(r'^uploadinfo/(\d+)$', views.uploadinfo),
    url(r'^getimgsrc$',views.getimgsrc),
    url(r'^clearcache$',views.clearcache),
]
