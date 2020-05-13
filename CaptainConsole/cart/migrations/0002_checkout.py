# Generated by Django 3.0.6 on 2020-05-12 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('Postal_code', models.FloatField()),
                ('Name_of_cardholder', models.CharField(max_length=999)),
                ('Card_number', models.CharField(max_length=16)),
                ('Expiration_date', models.DateField()),
                ('CVC', models.FloatField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]