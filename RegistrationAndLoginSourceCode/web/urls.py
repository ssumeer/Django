from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sitemap/$', views.sitemap, name='sitemap'),
    
]
