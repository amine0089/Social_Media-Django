from django.shortcuts import render, redirect
from .forms import SingUpForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse
from django.contrib.auth.models import User
from room.models import Room,Category
from django.db.models import Count
from django.contrib import messages

# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = SingUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username , password = password)
			login(request,user)
			return redirect('/')
		else:
			messages.error(request, 'An error occurred during registration')
	else:
		form = SingUpForm()
	context = {
			'form':form,
	}
	return render(request,'registration/singup.html',context)


def profile(request, slug):
	profile = Profile.objects.get(slug = slug)
	rooms = Room.objects.filter(owner = profile.id)
	category = Category.objects.annotate(num_items=Count('room'))
	context = {
				'profile': profile,
				'rooms':rooms,
				'category':category
	}
	return render(request,'accounts/profile.html',context)

def profile_edit(request):
	profile = Profile.objects.get(user = request.user)
	if request.method == "POST":
		userform = UserForm(request.POST,instance = request.user)
		profileform = ProfileForm(request.POST,request.FILES,instance = profile)
		if userform.is_valid() and profileform.is_valid():
			userform.save()
			myprofileform = profileform.save(commit = False)
			myprofileform.user = request.user
			myprofileform.save()
			return redirect('/')
	else:
		userform = UserForm(instance = request.user)
		profileform = ProfileForm(instance = profile)
	context = {
				'userform':userform,
				'profileform':profileform,
	}
	return render(request,'accounts/profileedit.html',context)