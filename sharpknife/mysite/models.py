import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class AppleAccountModel(models.Model):
    vpn_choice_list = (
        ('None', '不需要'),
        ('HK-1', '香港-1')
    )
    account_type_choice_list = (
        ('QY', '企业'),
        ('GR', '个人')
    )
    parse_type_choice_list = (
        ('None', '不做处理'),
        ('HX', '混淆1.0'),
        ('HX2', '混淆2.0'),
        ('JG', '加固'),
        ('SFJG', '第三方加固，混淆2.0'),
        ('SFCL', '第三方，原包')
    )
    status_choice_list = (
        ('NONE', '未使用'),
        ('DD', '等待审核'),
        ('ZZSH', '正在审核'),
        ('CW', '错误需要处理'),
        ('GB', '过包'),
        ('BDXX', '被动下线'),
        ('ZDXX', '主动下线')
    )
    apple_account = models.CharField(max_length=50, unique=True)
    email_pwd = models.CharField(max_length=50)
    apple_pwd = models.CharField(max_length=50)
    used = models.BooleanField(default=False,verbose_name='是否已使用')
    game_name = models.CharField(max_length=50, null=True,blank=True)
    vpn_name = models.CharField(
        max_length=50, blank=True,default='暂未设置',null=True)
    account_type = models.CharField(
        max_length=50, choices=account_type_choice_list, default='QY', null=False,verbose_name='帐号类型')
    use_device = models.CharField(
        max_length=50, null=True, verbose_name='使用的设备',blank=True)
    upload_date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='上传日期',blank=True,null=True)
    parse_type = models.CharField(
        max_length=50, choices=parse_type_choice_list, default='None', verbose_name='项目处理类型')
    small_game = models.BooleanField(default=False, verbose_name='是否为小游戏')
    status = models.CharField(
        max_length=200, choices=status_choice_list, default='NONE')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(
        'admin'), default='admin', to_field='username',verbose_name='使用者')
    remarks = models.TextField(null=True, blank=True,verbose_name='备注信息')
    create_date = models.DateField(auto_now=False, auto_now_add=True,verbose_name='帐号创建时间')
    

    def __str__(self):
        return str(self.apple_account)

    def get_queryset(self):
        queryset = self.get_queryset()
        queryset = queryset # TODO
        return queryset

    class Meta():
        verbose_name = "iOS帐号信息"
        ordering=['used']

    