from django.db import models


# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=35)
    password = models.CharField(max_length=18)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "name: " + self.name + " || email: " + self.email + " || password: " + self.password 

class Playlists(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.PROTECT)
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "name: " + self.name + " || User: " + self.user_id.name 

# class Songs(models.Model):
#     album_id = models.ForeignKey(to, on_delete)
#     artist_id = models.ForeignKey(to, on_delete)
#     name = models.CharField()
#     length = models.DecimalField()
#     def __str__(self):
#         return "Album: " + self.album_id.name + " || Artist: " + self.artist_id.name + " || Song Name: " + self.name + " || Length: " + self.length

