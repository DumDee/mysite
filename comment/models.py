from django.db import models
from django.contrib.auth.models import User
from song.models import Artist

class Comment(models.Model):
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(blank=True,default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
