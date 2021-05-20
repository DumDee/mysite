# Generated by Django 3.2.2 on 2021-05-14 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0003_song_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='songs_audio/', verbose_name='Песня'),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='songs_posters/', verbose_name='Изображение'),
        ),
    ]
