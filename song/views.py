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


# def song_create(request):
#     if request.method == "GET":
#         return render(request, 'SongCreate.html')

#     context ={}
  
#     form = SongCreateForm(request.POST or None, request.FILES)
#     if form.is_valid():
#         form.save()
          
#     context['form']= form
#     return render(request, "SongCreate.html", context)


# def song_edit(request, id):
#     if request.method == "GET":
#         s = Song.objects.get(id=id)
#         return render(request, 'SongEdit.html', {'song':s})

#     context ={}
#     obj = get_object_or_404(Song, id = id)

#     form = SongForm(request.POST or None, request.FILES, instance = obj)

#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/"+str(id))

#     context["form"] = form
#     context["song"] = obj

#     return render(request, "SongEdit.html", context)

# def song_delete(request, id):
#     s = get_object_or_404(Song, id = id)
#     s.delete()
#     return HttpResponseRedirect("/")