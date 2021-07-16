# Generated by Django 2.2.11 on 2021-05-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20210520_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='drivers',
            fields=[
                ('DriverCode', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='کد راننده')),
                ('Name', models.CharField(max_length=100, verbose_name='نام')),
                ('Family', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('Telephone', models.CharField(max_length=10, verbose_name='شماره همراه')),
                ('NationalCode', models.CharField(max_length=10, verbose_name='کد ملی')),
                ('LicensePlateNumber', models.CharField(max_length=200, verbose_name='شماره پلاک')),
                ('CarType', models.CharField(max_length=200, verbose_name='نوع ماشین')),
                ('FreightName', models.CharField(max_length=200, verbose_name='نام باربری')),
                ('AccountNumber', models.CharField(max_length=20, verbose_name='شماره حساب')),
                ('Shabanumber', models.CharField(max_length=24, verbose_name='شماره شبا')),
                ('CardNumber', models.CharField(max_length=16, verbose_name='شماره کارت')),
                ('Address', models.CharField(max_length=200, verbose_name='آدرس')),
                ('Description', models.TextField(max_length=200, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'راننده',
                'verbose_name_plural': 'راننده ها',
            },
        ),
    ]