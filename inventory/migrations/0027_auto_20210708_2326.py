# Generated by Django 2.2.11 on 2021-07-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0026_auto_20210622_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='Description',
            field=models.TextField(blank=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='TechnicalSpecifications',
            field=models.TextField(blank=True, verbose_name='مشخصات فنی'),
        ),
    ]
