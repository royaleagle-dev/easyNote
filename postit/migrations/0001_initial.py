# Generated by Django 3.2.3 on 2021-05-17 07:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=255)),
                ('note', models.CharField(max_length=255)),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]