from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.recognize_face, name="recognize_face"),
]