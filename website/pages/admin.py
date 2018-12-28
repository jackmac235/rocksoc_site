from django.contrib import admin
from .models import Event, News, Quote, Album_Category, Album, Image

class ImageAdmin(admin.TabularInline):
    model = Image
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
   inlines = [ImageAdmin,]

admin.site.register(Album,AlbumAdmin)

admin.site.register(Event)
admin.site.register(News)
admin.site.register(Quote)
admin.site.register(Album_Category)
#admin.site.register(Image)
