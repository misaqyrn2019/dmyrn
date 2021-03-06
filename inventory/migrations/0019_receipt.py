# Generated by Django 2.2.11 on 2021-06-14 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_changed_my_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='کد کالا')),
                ('Count', models.IntegerField(verbose_name='تعداد')),
                ('Amount', models.IntegerField(verbose_name='مبلغ جز')),
                ('TotalAmount', models.IntegerField(verbose_name='مبلغ کل')),
                ('Discount', models.IntegerField(verbose_name='تخفیف')),
                ('DiscountAmount', models.IntegerField(verbose_name='مبلغ تخفیف')),
                ('TotalAmountAfterDiscount', models.IntegerField(verbose_name='مبلغ کل پس از تخفیف')),
                ('Taxation', models.IntegerField(verbose_name='مالیات')),
                ('TaxAmount', models.IntegerField(verbose_name='مبلغ مالیات')),
                ('Date', models.DateTimeField(auto_now=True, verbose_name='تاریخ فاکتور')),
                ('IdCommodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Commodity', verbose_name='نام کالا')),
                ('IdUnitofMeasurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.UnitofMeasurement', verbose_name='واحد سنجش')),
            ],
            options={
                'verbose_name': 'فاکتور خرید/فروش',
                'verbose_name_plural': 'فاکتورهای خرید/فروش',
            },
        ),
    ]
