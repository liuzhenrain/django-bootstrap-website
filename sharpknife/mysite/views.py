from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
from .models import AppleAccountModel,AccountEventModel


def index(request):
    account_list = AppleAccountModel.objects.filter(
        used = True
    ).order_by('-upload_date')
    unused_list = AppleAccountModel.objects.filter(used=False)
    
    thead_list = ['帐号','游戏名称','VPN','帐号类型','设备','上传日期','处理方式','是否小游戏','状态','使用者']
    paginator = Paginator(account_list,25)
    contacts = paginator.get_page(0)
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


def listing(request):
    query_set = account_list = AppleAccountModel.objects.filter(
        used = True
    ).order_by('-upload_date')
    paginator = Paginator(query_set,25)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return HttpResponse('',content=contacts)
