from django.db import models


class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_tittle=models.CharField(max_length=250)
    genre=models.CharField(max_length=250)
    album_logo=models.CharField(max_length=500)


    def __str__(self):
        return self.album_tittle+' -- '+self.artist

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)