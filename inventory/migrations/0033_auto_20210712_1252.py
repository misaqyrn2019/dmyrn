# Generated by Django 2.2.11 on 2021-07-12 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0032_remove_receipt_totalamountafterdiscount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='DiscountAmount',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='TaxAmount',
        ),
    ]