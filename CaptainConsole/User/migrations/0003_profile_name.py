# Generated by Django 3.0.6 on 2020-05-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20200511_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]