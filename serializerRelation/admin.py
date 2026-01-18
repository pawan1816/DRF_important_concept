from django.contrib import admin
from .models import Song,Singer


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display=['id','name','gender']

@admin.register(Song)
class SingerAdmin(admin.ModelAdmin):
    list_display=['id','title','singer','duration']
