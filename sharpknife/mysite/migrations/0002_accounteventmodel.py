# Generated by Django 2.1.2 on 2018-10-22 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountEventModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_mes', models.CharField(max_length=1000)),
                ('event_date', models.DateField(auto_now=True, verbose_name='时间发生时间')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apple_event', to='mysite.AppleAccountModel')),
            ],
            options={
                'verbose_name': '苹果帐号事件',
                'verbose_name_plural': '苹果帐号事件',
                'ordering': ['-event_date'],
            },
        ),
    ]
