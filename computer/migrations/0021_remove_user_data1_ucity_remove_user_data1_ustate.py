# Generated by Django 4.1.9 on 2023-07-14 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0020_alter_user_data1_ufeedb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data1',
            name='ucity',
        ),
        migrations.RemoveField(
            model_name='user_data1',
            name='ustate',
        ),
    ]
