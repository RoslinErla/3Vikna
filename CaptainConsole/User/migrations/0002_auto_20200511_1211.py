# Generated by Django 3.0.6 on 2020-05-11 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.CharField(default='https://previews.123rf.com/images/alekseyvanin/alekseyvanin1704/alekseyvanin170403722/76700719-user-line-icon-profile-outline-vector-logo-illustration-linear-pictogram-isolated-on-white.jpg', max_length=9999),
        ),
    ]
