import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.


class AppleAccountModel(models.Model):
    account_type_choice_list = (
        ('QY', '企业'),
        ('GR', '个人'),
        ('QYQ', '企业签')
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
        ('NONE', '未提交'),
        ('DD', '等待审核'),
        ('ZZSH', '正在审核'),
        ('CW', '错误需要处理'),
        ('GB', '过包'),
        ('BDXX', '被动下线'),
        ('ZDXX', '主动下线'),
        ('SFCL', '三方处理中'),
        ('WXTS', '不需要提审'),
        ('ZZZZ', '正在制作')
    )
    apple_account = models.CharField(max_length=50, unique=True)
    email_pwd = models.CharField(max_length=50)
    apple_pwd = models.CharField(max_length=50)
    used = models.BooleanField(default=False, verbose_name='是否已使用')
    game_name = models.CharField(max_length=50, null=True, blank=True)
    vpn_name = models.CharField(
        max_length=50, blank=True, default='暂未设置', null=True)
    account_type = models.CharField(
        max_length=50, choices=account_type_choice_list, default='QY', null=False, verbose_name='帐号类型')
    use_device = models.CharField(
        max_length=50, null=True, verbose_name='使用的设备', blank=True)
    upload_date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='上传日期', blank=True, null=True)
    parse_type = models.CharField(
        max_length=50, choices=parse_type_choice_list, default='None', verbose_name='项目处理类型')
    small_game = models.BooleanField(default=False, verbose_name='是否为小游戏')
    status = models.CharField(
        max_length=200, choices=status_choice_list, default='NONE', verbose_name='帐号状态')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(
        'admin'), default='admin', to_field='username', verbose_name='使用者')
    remarks = models.TextField(null=True, blank=True, verbose_name='备注信息')
    create_date = models.DateField(
        auto_now=False, auto_now_add=True, verbose_name='帐号创建时间')
    request_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='申请使用时间')

    def __str__(self):
        return str(self.apple_account)

    class Meta():
        verbose_name = "iOS帐号信息"
        ordering = ['used']


class AccountEventModel(models.Model):
    """Apple Account Event Message."""

    event_mes = models.CharField(null=False, max_length=1000, verbose_name='事件')
    event_date = models.DateField(
        verbose_name='时间发生时间', auto_now=True, auto_now_add=False)
    account = models.ForeignKey(
        AppleAccountModel, on_delete=models.CASCADE, related_name='apple_event')
    who_add = models.ForeignKey(User, related_name='apple_event_who', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for AccountEventModel."""

        verbose_name = '苹果帐号事件'
        verbose_name_plural = '苹果帐号事件'
        ordering = ['-event_date']

    def __str__(self):
        """Unicode representation of AccountEventModel."""
        return self.event_mes
