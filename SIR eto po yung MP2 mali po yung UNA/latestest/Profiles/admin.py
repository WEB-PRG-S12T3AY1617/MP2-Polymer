# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User
from .models import Item

# Register your models here.

class ItemModelAdmin(admin.ModelAdmin):
    list_display = ["itemname", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_editable = ["itemname"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["itemname"]
    class Meta:
        model = Item

admin.site.register(Item, ItemModelAdmin)
admin.site.register(User)

