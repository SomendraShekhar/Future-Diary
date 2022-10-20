from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Post


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class CreatePostForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CreatePostForm, self).__init__(*args, **kwargs)
		self.fields['user'].widget.attrs.update({'class': 'form-group'})
		self.fields['title'].widget.attrs.update({'class': 'form-group'})
		self.fields['content'].widget.attrs.update({'class': 'form-group'})
		self.fields['url'].widget.attrs.update({'class': 'form-group'})
		self.fields['cat'].widget.attrs.update({'class': 'form-group'})

	class Meta:
		model = Post
		fields = ('user', 'post_id', 'title', 'content', 'url', 'cat', 'image')





class EditPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'content', 'cat', 'image')
