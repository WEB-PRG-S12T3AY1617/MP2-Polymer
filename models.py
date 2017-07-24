from django.db import models

class Details(models.Model):
    name_item= models.CharField(max_length=50)
    quantity_item = models.CharField(max_length=50)
    item_condition = models.CharField(max_length=50)
    item_type = models.CharField(max_length=50)
    item_logo = models.CharField(max_length=1000)
    course_name = models.CharField(max_length=10)
    tags_item = models.CharField(max_length=50)
    user_item = models.CharField(max_length=50)
    
    def __str__(self):
        return 'Name: ' + self.name_item
    
class User(models.Model):
    name = models.CharField(max_length=50)
    degree_program = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    
class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Item(models.Model):
    item = models.ForeignKey(Details, on_delete=models.CASCADE)
    

    

    
    