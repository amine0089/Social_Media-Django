from django.contrib import admin
from .models import Room,Category,Comment
# Register your models here.

admin.site.register(Room)
admin.site.register(Category)
admin.site.register(Comment)