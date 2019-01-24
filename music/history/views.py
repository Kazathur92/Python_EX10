from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Artist, Song, Album


def index(request):
  # return HttpResponse("Hello, world. You're at the polls index.")
  artist_list = Artist.objects.order_by('-dob_date')[:5]
  context = {'artist_list': artist_list}
  return render(request, 'history/index.html', context)

def artist_detail(request, artist_id):
  artist = get_object_or_404(Artist, pk=artist_id)
  album_set = Album.objects.filter(artist_id=artist_id)
  songs = Song.objects.filter(artist_id=artist_id)
  context = {'artist': artist, 'albums': album_set, 'songs': songs }
  return render(request, 'history/artist_detail.html', context)

def album_detail(request, album_id):
  album = get_object_or_404(Album, pk=album_id)
  # albumArtistId = get_object_or_404(Album, artist_id)
  # artist = Artist.objects.filter(artist_id=artist_id)
  # print(artist)
  song_set = Song.objects.filter(album_id=album_id)
  context = {'album': album, 'songs': song_set}
  return render(request, 'history/album_detail.html', context)

def addNewAlbum(request, artist_id):
  artist = Artist.objects.get(id=artist_id)
  # print(artist)
  title = request.POST['albumTitle']
  date = request.POST['albumDate']
  q = Album(album_name=title,release_year=date, artist=artist)
  q.save()
  return HttpResponseRedirect(reverse('history:artist_detail', args=(artist.id,)))




# Create your views here.
