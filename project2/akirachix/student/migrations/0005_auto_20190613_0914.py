# Generated by Django 2.2.2 on 2019-06-13 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20190612_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]