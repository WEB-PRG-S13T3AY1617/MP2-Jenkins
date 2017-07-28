from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
    
    #student or staff
    #degree programs or offices
    
    def __str__(self):
        return self.username
    
class DegreeProgram(models.Model):
    programname = models.CharField(max_length = 20)

class Office(models.Model):
    officesname = models.CharField(max_length = 50)
    
class Post(models.Model):
    ownername = models.ForeignKey(User, on_delete = models.CASCADE)
    itemname = models.CharField(max_length = 500)
    thumbnail = models.CharField(max_length = 1000)
    tags = models.CharField(max_length = 500)
    
    def __str__(self):
        return self.itemname

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    img = models.ForeignKey(Post, on_delete = models.CASCADE)
#    productname = models.ForeignKey(Posts, on_delete = models.CASCADE)
#    tags = models.ForeignKey(Posts, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)
    condition = models.CharField(max_length = 200)
    itemtype = models.CharField(max_length = 200)  
    #academic or office
    #course name if academic

