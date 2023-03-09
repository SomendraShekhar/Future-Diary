from gettext import Catalog
from turtle import pos, update
from urllib import response
from django import http
from django.contrib.auth.models import User
from blog.models import Post, Category,Comment
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm, CreatePostForm, EditPostForm,commentForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import categorySerializer,postSerializer,commentSerializer,createCategorySerializer,createCommentSerializer,createPostSerializer,createRegisterSerializer,registerSerializer,loginSerializer

class catSerializerView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = categorySerializer

class postSerializerView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = postSerializer

class commSerializerView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = commentSerializer

class registerSerializerView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = registerSerializer

class loginSerializerView(generics.ListCreateAPIView):
    pass

class createCatSerializerView(APIView):
    serializer_class = createCategorySerializer
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            cat_id = serializer.data.get('cat_id')
            title = serializer.data.get('title')
            description = serializer.data.get('description')
            url = serializer.data.get('url')
            image = serializer.data.get('image')
            queryset = Category.objects.filter(cat_id = cat_id)
            if queryset.exists():
                category = queryset[0]
                category.title = title
                category.description = description
                category.url = url
                category.image = image
                category.cat_id = cat_id
                category.save(update_fields= ['cat_id','title','description','url','image'])
                return Response(categorySerializer(category).data,status= status.HTTP_200_OK)
            else:
                category = Category(title=title,description=description,url=url,image=image)
                category.save()
                return Response(categorySerializer(category).data,status= status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
class createPostSerializerView(APIView):
    serializer_class = createPostSerializer
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            user = serializer.get('user')
            post_id = serializer.get('post_id')
            title = serializer.data.get('title')
            content = serializer.data.get('content')
            url = serializer.data.get('url')
            image = serializer.data.get('image')
            cat = serializer.data.get('cat')
            like = serializer.data.get('like')
            queryset = Post.objects.filter(url = url)
            if queryset.exists():
                post = queryset[0]
                post.user = user
                post.post_id = post_id
                post.title = title
                post.content = content
                post.url = url
                post.image = image
                post.cat = cat
                post.like = like
                post.save(update_fields= ['post_id','title','content','url','image','cat','like'])
                return Response(postSerializer(post).data,status= status.HTTP_201_CREATED)
            else:
                post = Post(post_id=post_id,title=title,content=content,url=url,image=image,cat=cat,like=like)
                post.save()
                return Response(postSerializer(post).data,status= status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

class createCommSerializerView(APIView):
    serializer_class = createCommentSerializer
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            commentedPost = serializer.get('commentedPost')
            name = serializer.data.get('name')
            comm = serializer.data.get('comm')
            queryset = Comment.objects.filter(commentedPost = commentedPost)
            if queryset.exists():
                comme = queryset[0]
                comme.commentedPost = commentedPost
                comme.name = name
                comme.comm = comm
                comme.save(update_fields= ['post_id','title','content','url','image','cat','like'])
                return Response(commentSerializer(comme).data,status= status.HTTP_201_CREATED)
            else:
                post = Comment(commentedPost=commentedPost,name=name,comm=comm)
                post.save()
                return Response(commentSerializer(post).data,status= status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

class createRegisterSerializerView(APIView):
    serializer_class = createRegisterSerializer
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            email = serializer.data.get('email')
            userCheck = User.objects.filter(username = username)
            emailCheck = User.objects.filter(email = email)
            if userCheck:
                return Response({'Bad Request': 'User already exist'}, status=status.HTTP_400_BAD_REQUEST)
            elif emailCheck:
                return Response({'Bad Request': 'Email already exist'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user = User(username = username,password = password, email = email)
                user.save()
                return Response(registerSerializer(user).data,status= status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

class checkLoginUser(APIView):
    serializer_class = loginSerializer
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {email}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")

    
        



def home(request, inEditMode=False,user=""):
    if not inEditMode:
        posts = Post.objects.all()[:11]
        cats = Category.objects.all()
    else:
        posts = Post.objects.filter(user=user)
        cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats,
        'inEditMode': inEditMode,
    }
    return render(request, 'home.html', data)


def post(request, url, commentBox = False):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats, 'commentBox': commentBox})


def category(request, url):
    cats = Category.objects.all()
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts,'cats':cats})


def register_request(request):
    cats = Category.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username Taken.")
            redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Used.")
            redirect('/register')
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('/')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form,'cats':cats})


def login_request(request):
    cats = Category.objects.all()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form,'cats':cats})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


def create_post_request(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    cats = Category.objects.all()

    if request.method == "POST":
        url = request.POST['url']
        title = request.POST['title']
        content = request.POST['content']
        cat = request.POST['cat']
        urlExist = Post.objects.filter(url=url).exists()
        if urlExist:
            messages.error(request, "Url already exist, please try different URl more related to your Theory")
            initialData = {
                'user': request.user,
                'title':title,
                'content':content,
                'cat':cat,
                'url':url
            }
            form = CreatePostForm(initial=initialData)
            return render(request=request, template_name="create_post.html",
                          context={"create_post_form": form, 'cats': cats})
        form = CreatePostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Theory Created Successfully.")
            return redirect('/')
    initialData = {
        'user': request.user,
    }
    form = CreatePostForm(initial=initialData)
    return render(request=request, template_name="create_post.html", context={"create_post_form": form,'cats':cats})


def edit_post_request(request, url):
    cats = Category.objects.all()
    obj = get_object_or_404(Post, url=url)
    form = EditPostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Theory Updated.")
        return redirect("/")

    return render(request, "edit_post.html", context={"edit_post_form": form,'cats':cats})


def Edit_Mode_request(request):
    user = request.user
    return home(request, inEditMode=True, user=user)


def like_request(request, url):
    post = Post.objects.get(url=url)
    current_url = request.META.get('HTTP_REFERER')
    current_url = current_url.split('/')

    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)

    if "Theory" in current_url:
        urls = "/Theory/"+url
        return redirect(urls)
    else:
        return HttpResponseRedirect(reverse('home'), False)


def comment_request(request,url):
    post = get_object_or_404(Post, url=url)
    initialData = {
        'commentedPost': get_object_or_404(Post, url=url),
        'name': request.user,
    }
    form = commentForm(request.POST or None,initial=initialData)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.commentedPost = post
        comment.save()
        messages.success(request, "comment added.")
        urls = "/Theory/" + url
        return redirect(urls)
    return render(request, "comment.html", context={"comment_form": form})

