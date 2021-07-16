# Generated by Django 2.2.11 on 2021-07-12 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0033_auto_20210712_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfersbetweenstoreroom',
            name='IdStoreroomDestination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StoreroomDestination', to='inventory.Storeroom', verbose_name='انبار مقصد'),
        ),
        migrations.AlterField(
            model_name='transfersbetweenstoreroom',
            name='IdStoreroomSource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StoreroomSource', to='inventory.Storeroom', verbose_name='انبار مبدا'),
        ),
    ]