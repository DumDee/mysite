from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from song.views import homepage, song_detail
from account.views import signin, signout, signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('<int:id>', song_detail),
    # path('edit/<int:id>', song_edit),
    # path('delete/<int:id>', song_delete),
    # path('create', song_create),
    path('account/signin', signin),
    path('account/signup', signup),
    path('account/signout', signout),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

