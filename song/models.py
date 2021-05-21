from django.db import models
import datetime

class Artist(models.Model):
    name = models.CharField("Название альбома", max_length=255)
    description = models.TextField(blank=True, default="")
    image = models.ImageField("Изображение", upload_to = "artist_image/", null=True, blank=True)
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField("Название альбома", max_length=100)
    image = models.ImageField("Изображение", upload_to = "album_posters/", null=True, blank=True)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)
    def __str__(self):
        return self.title



class Song(models.Model):
    title = models.CharField("Название песни", max_length=50)
    image = models.ImageField("Изображение", upload_to = "songs_posters/", null=True, blank=True)
    artist = models.ForeignKey(Artist, related_name='songs', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    ganre = models.CharField("Жанр", max_length=70)
    audio = models.FileField("Песня",upload_to = "songs_audio/", null = True, blank=True)
    url = models.SlugField(max_length=160, unique = True, null=True, blank=True )

    def __str__(self):
        return self.title


