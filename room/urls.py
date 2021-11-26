from django.urls import path
from . import views

app_name = "room"

urlpatterns = [
	path('',views.room_list, name = 'room_list'),
	path('create_room',views.create_room, name = 'create_room'),
	path('category=<slug:category>',views.searchin_by_category,name = 'searchin_by_category'),
	path('<str:slug>',views.room_detail, name = 'room_detail'),
]