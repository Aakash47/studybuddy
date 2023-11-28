from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Room(models.Model):
#     rslug = models.SlugField(unique=True)
#     ruser = models.ManyToManyField(User)
#     rname = models.CharField(max_length=100)
#     rdescriprtion = models.TextField()
#     rcourse = models.TextField()
#     rcollege = models.TextField()
#     rcreated_by = models.ForeignKey(User)
#     rcreated_on = models.DateTimeField()