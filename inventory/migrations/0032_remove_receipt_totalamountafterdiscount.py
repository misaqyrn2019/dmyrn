# Generated by Django 2.2.11 on 2021-07-12 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0031_remove_receipt_totalamount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='TotalAmountAfterDiscount',
        ),
    ]