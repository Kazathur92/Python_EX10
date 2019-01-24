import datetime
from django.db import models
from django.utils import timezone



class Artist(models.Model):
  artist_name = models.CharField(max_length=20)
  #  say_name = models.CharField(max_length=20)
  dob_date = models.CharField(max_length=4)

  def __str__(self):
    return self.artist_name

class Album(models.Model):
  album_name = models.CharField(max_length=20)
  release_year = models.CharField(max_length=20)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


  def __str__(self):
    return self.album_name


class Song(models.Model):
    song_name = models.CharField(max_length=20)
    release_year = models.CharField(max_length=20)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
      return self.song_name
# Create your models here.
