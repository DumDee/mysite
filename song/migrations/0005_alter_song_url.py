# Generated by Django 3.2.2 on 2021-05-14 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0004_auto_20210514_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='url',
            field=models.SlugField(blank=True, max_length=160, null=True, unique=True),
        ),
    ]
