# Generated by Django 2.2.11 on 2021-07-13 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0035_auto_20210713_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrepaired',
            name='IdCommodity',
            field=models.ForeignKey(default=30, on_delete=django.db.models.deletion.CASCADE, to='inventory.Commodity', verbose_name='نام کالا'),
        ),
    ]
