from django.db import models
import datetime

class Song(models.Model):
    title = models.CharField("Название песни", max_length=50)
    age = models.DateField("Дата выпуска", default = datetime.timedelta(0))
    image = models.ImageField("Изображение", upload_to = "songs_posters/", null=True, blank=True)
    artist = models.CharField("Исполнитель", max_length=50)
    album = models.CharField("Альбом", max_length=70)
    ganre = models.CharField("Жанр", max_length=70)
    audio = models.FileField("Песня",upload_to = "songs_audio/", null = True, blank=True)
    url = models.SlugField(max_length=160, unique = True, null=True, blank=True )

    def __str__(self):
        return self.title

