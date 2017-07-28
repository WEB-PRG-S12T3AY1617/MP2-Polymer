from django.conf.urls import url

from . import views

urlpatterns = [
    
    # /Profiles/
	url(r'^$', views.index, name='index'),
    
    # /Profiles/1/
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail' ),
    
    # /Profiles/itemdetail/1/1
    url(r'^itemdetail/(?P<item_id>[0-99]+)/$', views.itemdetail, name='itemdetail' ),
    
    # /Profiles/item/add
    url(r'item/add/$', views.ItemPost.as_view(), name='item-post'),
    
    # /Profiles/register
    url(r'register/$', views.Register.as_view(), name='register'),
    
    url(r'login/$', views.login ,name='login'),
    
    url(r'password/$', views.password ,name='password')
    
]