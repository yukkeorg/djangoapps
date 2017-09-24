from django.conf.urls import url

from . import views

app_name = "todo"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^append$', views.append, name='append'),
    url(r'^delete$', views.delete, name='delete'),
]
