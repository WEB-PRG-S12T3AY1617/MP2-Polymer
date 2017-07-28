from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class User(models.Model):
    profpic = models.FileField(default='/media/def.png')
    name = models.CharField(max_length=30 , default='')
    username = models.CharField(max_length=10 , default='')
    password = models.CharField(max_length=10 , default='')
    company = models.CharField(max_length=30 , default='')
    degree_Program = models.CharField(max_length=30 , default='')
    
    def get_absolute_url(self):
        return reverse('Profiles:detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name 

    
class Item(models.Model):
    itempic = models.FileField(default=True, null=True)
    itemname = models.CharField(max_length=30)
    quantity = models.IntegerField()
    itemtype = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)
    itemtag = models.CharField(max_length=20, default='')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.itemname 