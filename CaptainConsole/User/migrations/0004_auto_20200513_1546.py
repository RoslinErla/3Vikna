# Generated by Django 3.0.6 on 2020-05-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Name',
            field=models.CharField(blank=True, max_length=9999),
        ),
    ]
