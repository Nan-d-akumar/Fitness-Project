# Generated by Django 5.0 on 2024-01-30 10:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0011_remove_tbl_subcategory_reps_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_trainer',
            name='trainer_level',
            field=models.CharField(choices=[('', ''), ('level-1', 'level-1'), ('level-2', 'level-2'), ('level-3', 'level-3'), ('level-4', 'level-4'), ('level-5', 'level-5'), ('level-6', 'level-6')], default='', max_length=20),
        ),
        migrations.CreateModel(
            name='Tbl_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=3)),
                ('expiry_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('diet', models.FileField(null=True, upload_to='diet_pdf')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.FloatField(null=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.tbl_card')),
            ],
        ),
    ]
