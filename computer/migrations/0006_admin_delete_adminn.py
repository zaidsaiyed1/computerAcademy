# Generated by Django 4.1.9 on 2023-06-16 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0005_rename_admin_adminn'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.PositiveIntegerField()),
                ('aname', models.CharField(max_length=20)),
                ('apass', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='adminn',
        ),
    ]
