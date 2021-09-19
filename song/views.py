from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.http.response import HttpResponse
from .models import Artist, Song
from comment.models import Comment



def homepage(request):
    songlist = Artist.objects.all()
    context = {'xox': songlist}
    return render(request, "HomePage.html", context)

def song_detail(request, id):
    s = Artist.objects.get(id=id)
    com = s.comments.order_by('-created_at')
    return render(request, 'SongDetail.html', {'artist':s, 'comments': com})

