from django.shortcuts import render
from .models import Room, Category, Comment
from django.db.models import Count
from .forms import RoomForm, CommentForm
from django.core.paginator import Paginator
from django.db.models import Q



def room_list(request):
	room_list = Room.objects.all()
	search_query = request.GET.get('q')
	if search_query:
		room_list = room_list.filter(
			Q(title__icontains = search_query)|
			Q(description__icontains = search_query)
			)
	paginator = Paginator(room_list, 4)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	category = Category.objects.annotate(num_items=Count('room'))
	x = category.count()
	y = room_list.count()
	room_messages = Comment.objects.all().order_by('-id')[:5]
	context = {
		'room_list':page_obj,
		'category':category,
		'x':x,
		'room_messages':room_messages,
		'y':y
	}
	return render(request,'room/index.html',context)

def room_detail(request,slug):
	room_detail = Room.objects.get(slug = slug)
	participants = room_detail.participants.all()
	comment = reversed(Comment.objects.filter(room = room_detail))
	form = CommentForm()
	if request.method == 'POST':
		owner = request.user
		body = request.POST.get('body')
		rom = room_detail
		Comment.objects.create(user = request.user,body = body,room = rom)
		room_detail.participants.add(request.user)
	context = {
			'room_detail':room_detail,
			'comment':comment,
			'form':form,
			'participants':participants
	}
	return render(request,'room/roomdetail.html',context)

def create_room(request):
	category = Category.objects.all()
	form = RoomForm()

	if request.method =='POST':
		topic_name = request.POST.get('topic')
		topic, created = Category.objects.get_or_create(name=topic_name)
		title = request.POST.get('title')
		description = request.POST.get('description')
		Room.objects.create(owner = request.user,title = title,description=description, category = topic )
		

	context = {
			'form':form,
			'category': category
	}
	return render(request,'room/create-room.html',context)

def searchin_by_category(request,category):
	room_by_category = Room.objects.filter(category__name=category)
	context = {
		'room_list':room_by_category,
		}
	return render(request,'room/index.html',context)
