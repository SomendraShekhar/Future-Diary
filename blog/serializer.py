from rest_framework import serializers
from .models import Category, Post, Comment
from django.contrib.auth.models import User

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =('cat_id','title','description','url','image','add_date')

class createCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =('cat_id','title','description','url','image')

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user','post_id','title','content','url','cat','image','like')

class createPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user','post_id','title','content','url','cat','image','like')


class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =('commentedPost','name','comm')

class createCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =('commentedPost','name','comm')

class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('username','password','email')

class createRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('username','password','email')

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('password','email')

class createLoginSerializer(serializers.ModelSerializer):
     class Meta:
        model = User 
        fields = ('password','email')


