from django.contrib import admin
from .models import Users, Playlists, Artist

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
