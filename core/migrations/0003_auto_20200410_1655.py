# Generated by Django 3.0.5 on 2020-04-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200410_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='category_images/default.png', upload_to='category_images', verbose_name='Category Image'),
        ),
    ]
