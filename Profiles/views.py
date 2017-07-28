# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse        
from django.conf.urls import include
from django.template import loader
from .models import User
from .models import Item
from django.shortcuts import render , redirect 
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.

def index(request):
    all_users = User.objects.all()
    context = {
        'all_users': all_users
    }
    return render(request, 'Profiles/index.html', context)

def login(request):
    all_users = User.objects.all()
    context = {
        'all_users': all_users
    }
    return render(request, 'Profiles/login.html', context)

def password(request):
    all_users = User.objects.all()
    context = {
        'all_users': all_users
    }
    return render(request, 'Profiles/password.html', context)

def itemindex(request):
    all_items = Item.order_by('item.id')[:5]
    context = {
        'all_items': all_items
    }
    return render(request, 'Profiles/index.html', context)

def detail(request, user_id):
    try: 
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    context = {
        'user': user
    }
    return render(request, 'Profiles/detail.html', context)



def itemdetail(request, item_id):
    try: 
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Item Does Not Exist")
    context = {
        'item': item
    }
    return render(request, 'Profiles/itemdetail.html', context)


class ItemPost(CreateView):
    model = Item
    fields = ['itempic', 'itemname', 'quantity', 'itemtype', 'condition', 'seller']

class Register(CreateView):
    model = User
    fields = ['profpic', 'name', 'username', 'password', 'company', 'degree_Program']






            
            
            
            
            
            
            
            
            
            
            
            