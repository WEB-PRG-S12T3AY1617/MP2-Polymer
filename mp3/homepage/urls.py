from django.conf.urls import url

from . import views

urlpatterns = [
    
    # /homepage/
	url(r'^$', views.index, name='home'),
    
    url(r'in/$', views.indexin, name='homein'),
    
    url(r'viewallposts/$', views.viewallitem, name='viewallposts'),
    
    url(r'viewallpostsby15/$', views.viewallitemby15, name='viewallpostsby15'),
    
    url(r'viewallpostsby20/$', views.viewallitemby20, name='viewallpostsby20'),
    
]