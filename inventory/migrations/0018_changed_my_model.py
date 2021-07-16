# Generated by Django 2.2.11 on 2021-06-11 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_changed_my_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransfersbetweenStoreroom',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه انتقال')),
                ('Date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ثبت')),
                ('IdStoreroomDestination', models.IntegerField(verbose_name='انبار مقصد')),
                ('Description', models.TextField(max_length=200, verbose_name='توضیحات')),
                ('IdStoreroomSource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Storeroom', verbose_name='انبار مبدا')),
            ],
            options={
                'verbose_name': 'شناسه انتقال',
                'verbose_name_plural': 'انتقالات',
            },
        ),
    ]