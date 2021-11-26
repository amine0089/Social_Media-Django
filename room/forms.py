from django import forms
from .models import Room,Comment


class RoomForm(forms.ModelForm):
	class Meta:
		model = Room
		fields = '__all__'
		exclude = ('owner','slug')

		
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ["body"]