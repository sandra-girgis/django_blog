#sandra
# Create your models here.
from django.db import models
# Create your models here.
# models classes are tables
# first to create


#youmna
class Post(models.Model):
    Title = models.CharField(max_length = 100, null = False)
    Picture = models.CharField(max_length = 100, null = False)
    Content = models.CharField(max_length = 50, null = False)
    Date = models.DateTimeField()
    Likes = models.IntegerField(default=0)
    Dislikes = models.IntegerField(default=0)
    Post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.Title


#rehab
class Comment(models.Model):
    Text = models.CharField(max_length = 100, null = False)
    Time = models.DateTimeField()
    Post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def _str_(self):
        return self.Text

#sandra
class Postlike(models.Model):
    Islike = models.BooleanField(default=False)
    Isdislike = models.BooleanField(default=False)
    Post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Islike.boolean = True
    Isdislike.boolean = True