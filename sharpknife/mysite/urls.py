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
    path('account_modify/',mysite.IndexView.account_modify,name='account_modify'),
    path('account_choice_info/',mysite.IndexView.account_choice_info,name='account_choice_info'),
    path('get_account_unused/',mysite.IndexView.get_account_unused,name='get_account_unused'),
    path('request_account/',mysite.IndexView.request_account,name='request_account'),
]