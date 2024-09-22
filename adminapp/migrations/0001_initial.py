# Generated by Django 5.0 on 2024-01-18 11:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_fname', models.CharField(max_length=10)),
                ('staff_lname', models.CharField(max_length=10)),
                ('staff_age', models.CharField(max_length=3)),
                ('staff_gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other'), ('', '')], default='', max_length=10)),
                ('staff_phone', models.CharField(max_length=10)),
                ('staff_email', models.EmailField(max_length=254)),
                ('staff_status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
