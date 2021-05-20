# from django import forms
# from .models import Song
  
  
# class SongForm(forms.ModelForm):

#     class Meta:
#         model = Song
  
#         fields = [
#             "title",
#             "age",
#             "image",
#             "artist",
#             "album",
#             "ganre",
#             "audio",
#             "url",
#         ]

# class SongCreateForm(forms.ModelForm):
#     image = forms.ImageField(required=True)
#     audio = forms.FileField(required=True)
#     class Meta:
#         model = Song
  
#         fields = [
#             "title",
#             "age",
#             "image",
#             "artist",
#             "album",
#             "ganre",
#             "audio",
#             "url",
#         ]