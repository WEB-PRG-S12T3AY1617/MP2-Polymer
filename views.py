from django.http import Http404
from django.shortcuts import render
from .models import Details


def index(request):
    all_items = Details.objects.all()
    return render(request, 'items/index.html', {'all_items': all_items})

def detail(request, item_id):
    try:
        item = Details.objects.get(pk=item_id)
    except Details.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'items/detail.html', {'item': item})