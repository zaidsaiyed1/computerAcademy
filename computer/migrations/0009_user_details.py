# Generated by Django 4.1.9 on 2023-06-16 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0008_rename_adminsup_supadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('sex', models.PositiveIntegerField()),
                ('cp', models.IntegerField()),
                ('trestbps', models.IntegerField()),
                ('chol', models.IntegerField()),
                ('fbs', models.IntegerField()),
                ('restecg', models.IntegerField()),
                ('thalach', models.IntegerField()),
                ('exng', models.IntegerField()),
                ('oldpeak', models.IntegerField()),
                ('slp', models.IntegerField()),
                ('ca', models.IntegerField()),
                ('thal', models.IntegerField()),
                ('num', models.IntegerField()),
            ],
        ),
    ]
