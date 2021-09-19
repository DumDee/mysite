from song.views import song_detail
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Comment
from song.models import Artist
from django.contrib.auth.models import User

def add_comment(request,id):
    artist = get_object_or_404(Artist, pk=id)
    user = get_object_or_404(User, pk=request.user.id)
    text = request.POST['text']
    Comment(artist=artist, owner=user, text=text).save()
    return redirect(f"/{id}")


