# Generated by Django 2.2.11 on 2021-06-10 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_changed_my_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrycommodity',
            name='DateExpired',
            field=models.DateTimeField(default='2021-01-01', verbose_name='تاریخ انقضا'),
        ),
        migrations.AddField(
            model_name='entrycommodity',
            name='Serial',
            field=models.CharField(default='', max_length=200, verbose_name='سریال کالا'),
        ),
    ]
