from django.db import models


# Create your models here.
class Playlists(models.Model):
    created_by = models.ForeignKey('Users', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Playlist Name: " + self.name + " || Created By: " + self.created_by.name

class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=35)
    password = models.CharField(max_length=18)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "name: " + self.name + " || email: " + self.email + " || password: " + self.password 

class Artist(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return  "Artist Name: " + self.name

class Album(models.Model):
    artist_id = models.ForeignKey('Artist', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return "Album Name: " + self.name + " || Artist Name: " + self.artist_id.name


class Song(models.Model):
    album_id = models.ForeignKey('Album', on_delete=models.PROTECT, null=True)
    artist_id = models.ForeignKey('Artist', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=60)
    length = models.FloatField(null=True)

    def __str__(self):
        return 'Song Name: ' + self.name + ' || Artist Name: ' + self.artist_id.name + ' || Album Name: ' + self.album_id.name + ' || (Length: ' + str(self.length) + ' )'

