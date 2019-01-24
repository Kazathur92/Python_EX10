from django.urls import path

from . import views

app_name = 'history'

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/

    # the name of the route has to match the route in the template
    path('<int:artist_id>/', views.artist_detail, name='artist_detail'),
    # ex: /polls/5/results/
    path('albums/<int:album_id>/', views.album_detail, name='album_detail'),

    path('addNewAlbum/<int:artist_id>', views.addNewAlbum, name='addAlbum')
]