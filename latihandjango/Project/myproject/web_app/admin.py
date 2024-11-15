from django.contrib import admin
from .models import StatusModel, Album, Song, Author, Book, Vehicle, Car

admin.site.register(StatusModel)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Vehicle)
admin.site.register(Car)

# Register your models here.
