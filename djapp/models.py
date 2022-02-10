#sandra
# Create your models here.
from django.db import models
# Create your models here.
# models classes are tables
# first to create

#sandra
class Postlike(models.Model):
    Islike = models.BooleanField(default=False)
    Isdislike = models.BooleanField(default=False)
    Post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Islike.boolean = True
    Isdislike.boolean = True