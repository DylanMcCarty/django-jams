from django.contrib import admin
from .models import Users, Playlists, Artist, Album, Song

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Users, UsersAdmin)


class PlaylistsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Playlists, PlaylistsAdmin)


class ArtistAdmin(admin.ModelAdmin):
    pass
admin.site.register(Artist, ArtistAdmin)

class AlbumAdmin(admin.ModelAdmin):
    pass
admin.site.register(Album, AlbumAdmin)

class SongAdmin(admin.ModelAdmin):
    pass
admin.site.register(Song, SongAdmin)