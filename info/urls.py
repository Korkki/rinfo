"""info URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from base.api import views as base_views
from categories.api import views as categories_views
from links.api import views as links_views
from tags.api import views as tags_views

router = DefaultRouter()
router.register(r'category', categories_views.CategoryViewSet)
router.register(r'tag', tags_views.TagViewSet)
router.register(r'link', links_views.LinkViewSet)
router.register(r'user', base_views.UserViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/token/$', obtain_auth_token),
    url(r'^admin/', admin.site.urls),
]
