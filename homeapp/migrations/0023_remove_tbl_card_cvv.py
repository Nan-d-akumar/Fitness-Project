# Generated by Django 5.0 on 2024-03-27 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0022_tbl_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_card',
            name='cvv',
        ),
    ]
