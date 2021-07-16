# Generated by Django 2.2.11 on 2021-06-10 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_entrycommodity_invoicenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='کد حمل و نقل')),
                ('Sender', models.CharField(max_length=200, verbose_name='فرستند')),
                ('Transferee', models.CharField(max_length=200, verbose_name='گیرنده')),
                ('FreightNumber', models.IntegerField(verbose_name='شماره بارنامه')),
                ('SourceAddress', models.CharField(max_length=200, verbose_name='آدرس مبدا')),
                ('Date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ثبت')),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('IdDrivers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.drivers', verbose_name='نام راننده')),
            ],
            options={
                'verbose_name': 'حمل و نقل',
                'verbose_name_plural': 'حمل و نقل',
            },
        ),
        migrations.RemoveField(
            model_name='entrycommodityupdate',
            name='entrycommodity_ptr',
        ),
        migrations.AlterField(
            model_name='entrycommodity',
            name='InvoiceNumber',
            field=models.CharField(max_length=200, verbose_name='شماره فاکتور'),
        ),
        migrations.DeleteModel(
            name='EntryCommodityCreate',
        ),
        migrations.DeleteModel(
            name='EntryCommodityUpdate',
        ),
    ]