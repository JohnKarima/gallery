# Generated by Django 3.1.2 on 2020-10-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0006_auto_20201011_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='gallery_image',
            field=models.ImageField(null=True, upload_to='gallery/'),
        ),
    ]
