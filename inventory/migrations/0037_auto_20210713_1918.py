# Generated by Django 2.2.11 on 2021-07-13 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0036_auto_20210713_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='productrepaired',
            name='Status',
            field=models.CharField(choices=[('Y', 'تعمیر شده'), ('N', 'تعمیر نشده')], default='N', max_length=1, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='productrepaired',
            name='IdCommodity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Commodity', verbose_name='نام کالا'),
        ),
    ]
