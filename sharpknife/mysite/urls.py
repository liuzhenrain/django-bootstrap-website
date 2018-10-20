from django.urls import path
from . import views as mysite

app_name = 'mysite'

urlpatterns = [
    path("",mysite.index,name='index'),
    path('index/',mysite.index,name='index'),
    path('ios/',mysite.ios,name='ios'),
    path('update/',mysite.update,name='update')
]