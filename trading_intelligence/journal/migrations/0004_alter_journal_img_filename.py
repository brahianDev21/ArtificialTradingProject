# Generated by Django 5.1.2 on 2024-11-07 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_alter_journal_img_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='img_filename',
            field=models.ImageField(upload_to='trading_intelligence_proyect/trading_intelligence/files/journal_imgs'),
        ),
    ]