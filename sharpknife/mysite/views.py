from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.utils import timezone
from django.views import generic
from django.core import serializers
import json,datetime

# Create your views here.
from .models import AppleAccountModel,AccountEventModel


def index(request):
    account_list = AppleAccountModel.objects.filter(
        used = True
    ).order_by('-upload_date')
    unused_list = AppleAccountModel.objects.filter(used=False)
    
    thead_list = ['帐号','游戏名称','VPN','帐号类型','设备','上传日期','处理方式','是否小游戏','状态','使用者']
    paginator = Paginator(account_list,10)

    page = request.GET.get('page')
    if page != None:
        contacts = paginator.get_page(page)
    else:
        contacts = paginator.get_page(1)
    context = {
        'account_list':account_list,
        'unused_list':unused_list,
        'thead_list':thead_list,
        'contacts':contacts,
    }
    return render(request, "mysite/index.html",context=context)


def ios(request):
    return render(request, "mysite/ios.html")


def update(request):
    return render(request, "mysite/update.html")

class BaseView(object):
    timestep = timezone.now()


class IndexView(BaseView):
    def index(request):
        account_list = AppleAccountModel.objects.filter(
            used = True
        ).order_by('-upload_date')
        unused_list = AppleAccountModel.objects.filter(used=False)
        
        thead_list = ['帐号','游戏名称','VPN','帐号类型','设备','上传日期','处理方式','是否小游戏','状态','使用者']
        paginator = Paginator(account_list,10)

        page = request.GET.get('page')
        if page != None:
            contacts = paginator.get_page(page)
        else:
            contacts = paginator.get_page(1)
        context = {
            'account_list':account_list,
            'unused_list':unused_list,
            'thead_list':thead_list,
            'contacts':contacts,
            'timestep':timezone.now(),
        }
        return render(request, "mysite/index.html",context=context)
    
    def used_account_json(request):
        account_list = AppleAccountModel.objects.filter(
            used = True
        ).order_by('-request_date')
        json_data={
            'total':len(account_list),
            'rows': []
        }
        for item in account_list:
            json_data['rows'].append({
                'id':item.id,
                'apple_account':item.apple_account,
                'game_name':item.game_name,
                'vpn_name':item.vpn_name,
                'account_type':item.get_account_type_display(),
                'use_device':item.use_device,
                'upload_date': item.upload_date.strftime('%Y-%m-%d') if item.upload_date!=None else "",
                'parse_type':item.get_account_type_display(),
                'small_game':item.small_game,
                'status':item.get_status_display(),
                'user':item.user.username,
            })
        return JsonResponse(json_data,safe=False)

