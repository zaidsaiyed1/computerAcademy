# Generated by Django 4.1.9 on 2023-07-15 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0023_alter_user_data1_uemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data1',
            name='ucountry',
            field=models.CharField(default='NUll', max_length=20),
        ),
        migrations.AlterField(
            model_name='user_data1',
            name='uemail',
            field=models.EmailField(default='NUll', max_length=60),
        ),
        migrations.AlterField(
            model_name='user_data1',
            name='uname',
            field=models.CharField(default='NUll', max_length=30),
        ),
    ]