# Generated by Django 2.2.11 on 2021-05-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_storeroom_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('AccountSideCode', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='کد طرف حساب')),
                ('Name', models.CharField(max_length=100, verbose_name='نام')),
                ('Family', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('Mobile', models.TextField(verbose_name='شماره موبایل')),
                ('Telephone', models.TextField(verbose_name='شماره تلفن')),
                ('RegistrationNumber', models.TextField(verbose_name='شماره ثبت')),
                ('EconomicNumber', models.TextField(verbose_name='کدملی/شماره اقتصادی')),
                ('NationalID', models.TextField(verbose_name='شناسه ملی')),
                ('PostalCode', models.TextField(verbose_name='کد پستی')),
                ('Address', models.TextField(verbose_name='آدرس')),
                ('FirstBalanceCourse', models.TextField(verbose_name='مانده اول دوره')),
            ],
            options={
                'verbose_name': 'نام مشتری',
                'verbose_name_plural': 'مشتری ها',
            },
        ),
        migrations.AddField(
            model_name='storeroom',
            name='Telephone',
            field=models.TextField(default='12', verbose_name='شماره تلفن'),
        ),
    ]
