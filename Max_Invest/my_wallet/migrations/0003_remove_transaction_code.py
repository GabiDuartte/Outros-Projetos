# Generated by Django 4.2 on 2023-06-27 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_wallet', '0002_alter_transaction_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='code',
        ),
    ]
