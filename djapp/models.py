#sandra
# Create your models here.
from django.db import models

# Create your models here.
# models classes are tables
# first to create

#omar
class Category(models.Model):
    Name = models.CharField(max_length = 50, null = False) 
    # Category object
    def __str__(self):
        return self.Name
#omar
class User(models.Model):
    Username = models.CharField(max_length = 50, null = False)
    Password = models.CharField(max_length = 50, null = False)
    Email = models.EmailField(max_length = 50, null = False) # @ . 
    Isadmin = models.BooleanField(default=False) # boolean True False
    Isblocked = models.BooleanField(default=False) # boolean True False
    Categories = models.ManyToManyField(Category) # many to many relationship
    def __str__(self):
        return self.Username
    # ui for true and false advanced
    Isadmin.boolean = True 
    Isblocked.boolean = True
    
#reem
class Tag(models.Model):
    Name = models.CharField(max_length = 50, null = False)
    def __str__(self):
        return self.Name
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
    def __str__(self):
        return self.Text
    
#samah
class Word(models.Model):
    Name = models.CharField(max_length = 50, null = False)
    def __str__(self):
        return self.Name
#sandra
class Postlike(models.Model):
    Islike = models.BooleanField(default=False)
    Isdislike = models.BooleanField(default=False)
    Post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Islike.boolean = True
    Isdislike.boolean = True