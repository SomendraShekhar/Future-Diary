from django.contrib.auth.models import User
from blog.models import Post, Category
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm, CreatePostForm, EditPostForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})


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
        form = CreatePostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            messages.success(request, "Theory Created Successfully.")
            return redirect('/')
    initialData = {
        'user': request.user,
    }
    print(request.user)
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
    print(current_url)

    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)

    if "Theory" in current_url:
        urls = "/Theory/"+url
        return redirect(urls)
    else:
        return HttpResponseRedirect(reverse('home'), False)

