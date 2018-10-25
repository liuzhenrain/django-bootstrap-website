from django.urls import path
from . import views as mysite

app_name = 'mysite'

urlpatterns = [
    path("",mysite.IndexView.index,name='index'),
    path('index/',mysite.IndexView.index,name='index'),
    path('ios/',mysite.ios,name='ios'),
    path('update/',mysite.update,name='update'),
    path('account_json/',mysite.IndexView.used_account_json,name='account_json'),
    path('login/',mysite.IndexView.login,name='login'),
    path('logout/',mysite.IndexView.logout,name='logout'),
]