# Generated by Django 5.0.2 on 2024-03-07 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='contact',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='fullname',
            field=models.CharField(max_length=250),
        ),
    ]
