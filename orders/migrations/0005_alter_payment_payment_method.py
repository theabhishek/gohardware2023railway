# Generated by Django 4.0.3 on 2022-09-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_payment_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('RazorPay', 'RazorPay'), ('CashOnDelivery', 'CashOnDelivery')], max_length=100),
        ),
    ]