"""
URL configuration for NewsReadingApp_Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from routers import router

from apps.login.views import LoginView
from apps.articles.views import SummarizeView
from apps.followers.views import followers_list, following_list
from apps.categories.views import articles_by_category
from apps.notifications.views import user_notifications

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'core_api'), namespace='core_api')),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/summary/', SummarizeView.as_view(), name='summary'),
    path('api/followers/', followers_list, name='follower_list'),
    path('api/following/', following_list, name='following_list'),
    path('articles/category/', articles_by_category, name='articles_by_category'),
    path('api/user_notifications/', user_notifications, name='article_publish_notification'),
]
