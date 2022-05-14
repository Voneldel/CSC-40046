from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^home/$', views.home, name='home'),
]