# Generated by Django 4.1.9 on 2023-06-16 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0002_alter_admin_aid_alter_admin_apass'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='admin',
            new_name='Supadmin',
        ),
    ]