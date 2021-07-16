# Generated by Django 2.2.11 on 2021-05-21 18:29

import account.mixins
from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.edit
import inventory.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_drivers'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryCommodity',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='کد کالا')),
                ('Count', models.IntegerField(verbose_name='تعداد')),
                ('DateEntry', models.DateTimeField(verbose_name='تاریخ')),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('IdCommodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Commodity', verbose_name='نام کالا')),
                ('IdCustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Customer', verbose_name='نام مشتری')),
                ('IdStoreroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Storeroom', verbose_name='نام انبار')),
            ],
            options={
                'verbose_name': 'ورود کالا',
                'verbose_name_plural': 'ورود کالاها',
            },
        ),
        migrations.CreateModel(
            name='EntryCommodityCreate',
            fields=[
                ('entrycommodity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.EntryCommodity')),
            ],
            bases=(account.mixins.SuperUserAccessMixin, inventory.mixins.StorekeeperUserAccessMixin, 'inventory.entrycommodity', django.views.generic.edit.CreateView),
        ),
        migrations.CreateModel(
            name='EntryCommodityUpdate',
            fields=[
                ('entrycommodity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.EntryCommodity')),
            ],
            bases=(account.mixins.SuperUserAccessMixin, inventory.mixins.StorekeeperUserAccessMixin, 'inventory.entrycommodity', django.views.generic.edit.UpdateView),
        ),
    ]
