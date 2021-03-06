# Generated by Django 2.2.1 on 2019-06-01 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('registration_number', models.CharField(max_length=20)),
                ('place_of_residence', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=15)),
                ('gmail', models.EmailField(max_length=254)),
                ('id_number', models.IntegerField(max_length=20)),
            ],
        ),
    ]
