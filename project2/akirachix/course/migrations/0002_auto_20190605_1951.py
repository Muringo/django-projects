# Generated by Django 2.2.2 on 2019-06-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration_in_months',
            field=models.IntegerField(),
        ),
    ]
