# Generated by Django 2.2.1 on 2019-06-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id_number',
            field=models.IntegerField(),
        ),
    ]
