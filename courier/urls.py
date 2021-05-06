"""courier URL Configuration

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
from django.urls import path

from news import views

urlpatterns = [
    path('article/<int:post_id>/', views.article_detail),
    path('author/<int:author_id>/', views.author_detail),
    path('', views.index),
    path('admin/', admin.site.urls),
]

"""localhost:8000/admin
localhost:8000/author/3/
localhost:8000/author/00000/
localhost:8000/article/2/

"""