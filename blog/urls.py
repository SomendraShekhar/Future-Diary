"""iblogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import catSerializerView, commSerializerView, postSerializerView, createCatSerializerView, createCommSerializerView, createPostSerializerView,registerSerializerView,createRegisterSerializerView

urlpatterns = [
    path('cat', catSerializerView.as_view()),
    path('post', postSerializerView.as_view()),
    path('comm', commSerializerView.as_view()),
    path('create-cat', createCatSerializerView.as_view()),
    path('create-post', createPostSerializerView.as_view()),
    path('create-comm', createCommSerializerView.as_view()),
    path('register',registerSerializerView.as_view()),
    path('create-register',createRegisterSerializerView.as_view())

    
]
# urlpatterns = [
#     path('', home,name="home"),
#     path('Theory/<slug:url>', post, name="Theory"),
#     path('category/<slug:url>', category),
#     path("register", register_request),
#     path("login", login_request),
#     path("logout", logout_request),
#     path("newTheory", create_post_request),
#     path("editTheory/<slug:url>", edit_post_request),
#     path('editMode', Edit_Mode_request),
#     path("likes/<slug:url>", like_request),
#     path('Theory/<slug:url>/comment', comment_request,name='comment')
# ]