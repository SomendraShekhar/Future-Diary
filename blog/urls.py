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
from .views import home, post, category, register_request, login_request, logout_request, create_post_request, edit_post_request,Edit_Mode_request,like_request

urlpatterns = [
    path('', home,name="home"),
    path('Theory/<slug:url>', post,name = "Theory"),
    path('category/<slug:url>', category),
    path("register", register_request),
    path("login", login_request),
    path("logout", logout_request),
    path("newTheory", create_post_request),
    path("editTheory/<slug:url>", edit_post_request),
    path('editMode', Edit_Mode_request),
    path("likes/<slug:url>", like_request)
]
