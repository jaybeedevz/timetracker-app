from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('smne', views.smne, name='smne'),
    path('shang', views.shang, name='shang'),
    path('rpm', views.rpm, name='rpm'),
    path('filomena', views.filomena, name='filomena'),
    path('venice', views.venice, name='venice'),
    path('dd', views.dd, name='dd'),
    path('alabang', views.alabang, name='alabang'),
    path('cybergate', views.cybergate, name='cybergate'),
    path('galleria', views.galleria, name='galleria'),

]