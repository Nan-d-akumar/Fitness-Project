# Generated by Django 5.0 on 2023-12-22 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0005_alter_tbl_customer_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_trainer',
            name='trainer_image',
            field=models.ImageField(default='', upload_to='trainer_images'),
        ),
        migrations.AlterField(
            model_name='tbl_trainer',
            name='trainer_certificate',
            field=models.FileField(upload_to='trainer_certificates'),
        ),
    ]
