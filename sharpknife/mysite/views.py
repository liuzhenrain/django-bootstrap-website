from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
from .models import AppleAccountModel, AccountEventModel


def index(request):
    account_list = AppleAccountModel.objects.filter(
        used=True
    ).order_by('-upload_date')
    unused_list = AppleAccountModel.objects.filter(used=False)

    thead_list = ['帐号', '游戏名称', 'VPN', '帐号类型',
                  '设备', '上传日期', '处理方式', '是否小游戏', '状态', '使用者']
    paginator = Paginator(account_list, 10)

    page = request.GET.get('page')
    if page != None:
        contacts = paginator.get_page(page)
    else:
        contacts = paginator.get_page(1)
    context = {
        'account_list': account_list,
        'unused_list': unused_list,
        'thead_list': thead_list,
        'contacts': contacts,
    }
    return render(request, "mysite/index.html", context=context)

@login_required
def ios(request):
    # print(request.user.is_authenticated)
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    # else:
    return render(request, "mysite/ios.html")


def update(request):
    return render(request, "mysite/update.html")


class BaseView(object):
    timestep = timezone.now()


class IndexView(BaseView):
    def index(request):
        account_list = AppleAccountModel.objects.filter(
            used=True
        ).order_by('-upload_date')
        unused_list = AppleAccountModel.objects.filter(used=False)

        thead_list = ['帐号', '游戏名称', 'VPN', '帐号类型',
                      '设备', '上传日期', '处理方式', '是否小游戏', '状态', '使用者']
        paginator = Paginator(account_list, 10)

        page = request.GET.get('page')
        if page != None:
            contacts = paginator.get_page(page)
        else:
            contacts = paginator.get_page(1)
        context = {
            'account_list': account_list,
            'unused_list': unused_list,
            'thead_list': thead_list,
            'contacts': contacts,
            'timestep': timezone.now(),
        }
        return render(request, "mysite/index.html", context=context)

    def used_account_json(request):
        account_list = AppleAccountModel.objects.filter(
            used=True).order_by('-request_date')
        json_data = {
            'total': len(account_list),
            'rows': []
        }
        for item in account_list:
            json_data['rows'].append({
                'id': item.id,
                'apple_account': item.apple_account,
                'game_name': item.game_name,
                'vpn_name': item.vpn_name,
                'account_type': item.get_account_type_display(),
                'use_device': item.use_device,
                'upload_date': item.upload_date.strftime('%Y-%m-%d') if item.upload_date != None else "",
                'parse_type': item.get_account_type_display(),
                'small_game': item.small_game,
                'status': item.get_status_display(),
                'user': item.user.username,
            })
        return JsonResponse(json_data, safe=False)

    def login(request):
        if request.method == 'GET':
            context = {
                'from_page':request.get_full_path,
            }
            return render(request,'mysite/login.html',context=context)
        else:
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = auth.authenticate(request=request,username=username,password=password)
                if user is not None:
                    auth.login(request,user)
                    if request.POST.get('next'):
                        nextpath = request.POST.get('next')
                        return redirect(nextpath)
                    else:
                        if user.is_staff:
                            return redirect('/admin')
                        return render(request,'mysite/index.html')
                else:
                    context = {
                        'error':'登录失败，请重试'
                    }
                    return render(request,'mysite/login.html',context=context)
            except KeyError as identifier:
                context = {
                    'error':'登录失败，请重试'
                }
                return render(request,'mysite/login.html',context=context)
    
    def logout(request):
        auth.logout(request)
        return redirect("/")

    def account_modify(request):
        account_id = request.POST.get('id')
        game_name = request.POST.get('game_name')
        vpn_name = request.POST.get('vpn_name')
        use_device = request.POST.get('use_device')
        upload_date = request.POST.get('upload_date')
        parse_type = request.POST.get('parse_type')
        small_game = request.POST.get('small_game')
        status = request.POST.get('status')

        item_model = AppleAccountModel.objects.get(id=account_id)
        try:
            # item_model.update(game_name=game_name,vpn_name=vpn_name,use_device=use_device,upload_date=upload_date,parse_type=parse_type,small_game=small_game,status = status)
            item_model.game_name = game_name
            item_model.vpn_name = vpn_name
            item_model.use_device = use_device
            if not upload_date.strip() == "":
                item_model.upload_date = upload_date
            item_model.parse_type = parse_type
            item_model.small_game = small_game
            item_model.status = status
            item_model.save()
            return redirect("/")
        except Exception as e:
            print(e)
            context = {
                'error':'出现错误，无法进行修改',
                'exception':e.__str__(),
            }
            return JsonResponse(context,safe=False)

    def account_choice_info(request):
        context = {
            'parse_type_choice':AppleAccountModel.parse_type_choice_list,
            'status_choice':AppleAccountModel.status_choice_list,
        }
        return JsonResponse(context,safe=False)

    def get_account_unused(request):
        account_list = AppleAccountModel.objects.filter(
            used=False).order_by('-create_date')
        json_data = {
            'total': len(account_list),
            'rows': []
        }
        for item in account_list:
            json_data['rows'].append({
                'id': item.id,
                'apple_account': item.apple_account,
                'account_type': item.get_account_type_display(),
            })
        return JsonResponse(json_data, safe=False)

    def request_account(request):
        if request.method == 'POST':
            account_id = request.POST.get('id')
            if not account_id.strip() == "":
                account = AppleAccountModel.objects.get(id=account_id)
                if account:
                    # account.used = True
                    success = {
                        'apple_account':account.apple_account,
                        'email_pwd':account.email_pwd,
                        'apple_pwd':account.apple_pwd,
                    }
                    return JsonResponse({'success':success},safe=False)
                else:
                    return JsonResponse({'error':'没有该帐号信息'},safe=False)
        else:
            return JsonResponse({'error':"获取失败"},safe=False)
            


