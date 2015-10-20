from django.conf.urls import url
from links.views import LinksList

urlpatterns = [
    url(r'$', LinksList.as_view(), name='link_list'),
]