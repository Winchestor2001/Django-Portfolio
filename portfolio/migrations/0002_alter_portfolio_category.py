# Generated by Django 3.2.8 on 2021-10-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(choices=[('Web Site', 'Web'), ('Telegram Bot', 'TgBot')], max_length=100),
        ),
    ]