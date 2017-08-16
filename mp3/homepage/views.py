# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse        
from django.conf.urls import include
from django.template import loader
from Profiles.models import User
from Profiles.models import Item
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages


# Create your views here.

def index(request):
    all_items = Item.objects.all()[:10]
    context = {
        'all_items': all_items
    }
    return render(request, 'homepage/home.html', context)

def indexin(request):
    all_items = Item.objects.all()[:10]
    context = {
        'all_items': all_items
    }
    return render(request, 'homein.html', context)

def itemdetail(request, item_id):
    try: 
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Item Does Not Exist")
    context = {
        'item': item,
    }
    return render(request, 'Profiles/itemdetail.html', context)

def userdetail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    context = {
        'user': user,
    }
    return render(request, 'Profiles/detail.html', context)

def viewallitem(request):
    queryset_list = Item.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(itemtag__icontains=query)
            
    paginator = Paginator(queryset_list, 10) # Shows 10 items per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
        
    context = {
        "all_items": queryset,
        "page_request_var": page_request_var
        }
    return render(request, 'homepage/viewallposts.html', context)

def viewallitemby15(request):
    queryset_list = Item.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(itemtag__icontains=query)
            
    paginator = Paginator(queryset_list, 15) # Shows 15 items per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
        
    context = {
        "all_items": queryset,
        "page_request_var": page_request_var
        }
    return render(request, 'homepage/viewallpostsby15.html', context)


def viewallitemby20(request):
    queryset_list = Item.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(itemtag__icontains=query)
            
    paginator = Paginator(queryset_list, 20) # Shows 20 items per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
        
    context = {
        "all_items": queryset,
        "page_request_var": page_request_var
        }
    return render(request, 'homepage/viewallpostsby20.html', context)