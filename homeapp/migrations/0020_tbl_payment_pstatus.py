# Generated by Django 5.0 on 2024-02-16 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0019_alter_tbl_trainer_assign_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_payment',
            name='pstatus',
            field=models.BooleanField(default=True),
        ),
    ]
