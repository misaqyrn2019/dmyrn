# Generated by Django 2.2.11 on 2021-06-10 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_changed_my_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrycommodity',
            name='Status',
            field=models.CharField(choices=[('i', 'ورود'), ('o', 'خروج')], default='i', max_length=1, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='entrycommodity',
            name='DateExpired',
            field=models.DateTimeField(verbose_name='تاریخ انقضا'),
        ),
        migrations.AlterField(
            model_name='entrycommodity',
            name='Serial',
            field=models.CharField(max_length=200, verbose_name='سریال کالا'),
        ),
    ]
