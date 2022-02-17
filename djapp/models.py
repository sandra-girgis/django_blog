#sandra
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
import django.utils
#omar
class Category(models.Model):
    Name = models.CharField(max_length = 50, null = False) 
    # Category object
    def __str__(self):
        return self.Name
#reem
class Tag(models.Model):
    Name = models.CharField(max_length = 50, null = False,)
    def __str__(self):
        return self.Name

#youmna
class Post(models.Model):
    Title = models.CharField(max_length = 100, null = False)
    Picture = models.ImageField(upload_to='img/')
    Content = models.TextField(max_length = 4000, null = False)
    Date = models.DateTimeField(default=django.utils.timezone.now)
    Likes = models.IntegerField(default=0)
    liked = models.ManyToManyField(User, default=None,blank=True,related_name='liked')
    # disliked = models.ManyToManyField(User, default=None,blank=True,related_name='disliked')
    Dislikes = models.IntegerField(default=0)
    Post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author')
    Tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.Title
    @property    
    def num_likes(self):
        return self.liked.all().count()    

#rehab
class Comment(models.Model):
    Text = models.CharField(max_length = 100, null = False)
    Time = models.DateTimeField(default=django.utils.timezone.now)
    Post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.Text

#samah
class Word(models.Model):
    Name = models.CharField(max_length = 50, null = False)
    def __str__(self):
        return self.Name

#sandra
LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)

# DISLIKE_CHOICES = (
#     ('Dislike','Dislike'),
#     ('Cancel_Dislike','Cancel_Dislike'),
# )
class Postlike(models.Model):
    Islike = models.BooleanField(default=False)
    Isdislike = models.BooleanField(default=False)
    Post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Islike.boolean = True
    Isdislike.boolean = True
    value = models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)
    # value1 = models.CharField(choices=DISLIKE_CHOICES,default='Dislike',max_length=50)
  


class CategoryMembership(models.Model):
    userr = models.ForeignKey(User,on_delete=models.CASCADE)
    categoryy = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.userr.username + " subscribed To " +self.categoryy.Name

