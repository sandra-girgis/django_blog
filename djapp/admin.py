#sandra
from django.contrib import admin
from .models import *
#reem
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ['User Details',{'fields':['Username','Password','Email','Isadmin','Isblocked']}], #show on create
    )
    list_display = ('Username','Password','Email','Isadmin','Isblocked') # show users list
    list_filter = ['Username','Email','Isadmin','Isblocked'] # advanced
    search_fields = ['Username','Email','Isadmin','Isblocked'] # advanced
#reem
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Category Details',{'fields':['Name']}],
    )
    list_display = ('Name',)
    search_fields = ['Name']
#youmna
class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Category Details',{'fields':['Name']}],
    )
    list_display = ('Name',)
    search_fields = ['Name']

#omar
class PostAdmin(admin.ModelAdmin):
    fieldsets = ( # picture is string [url]
        ['User Details',{'fields':['Title','Picture','Content','Post_category','User_id','Tags']}], #'Likes','Dislikes','Date',
    )
    list_display = ('Title','Picture','Content','Likes','Dislikes','Post_category','User_id') #'Date',
#samah
class PostlikeAdmin(admin.ModelAdmin):
    fieldsets = (
        ['User Details',{'fields':['Islike','Isdislike','Post_id','User_id']}],
    )
    list_display = ('Islike','Isdislike','Post_id','User_id')
#rehab
class WordAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Category Details',{'fields':['Name']}],
    )
    list_display = ('Name',)
    search_fields = ['Name']
#sandra
class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        ['User Details',{'fields':['Text','Post_id','User_id']}], #'Time',
    )
    list_display = ('Text','Post_id','User_id') #'Time',

# to show the tables in the site
#reem
admin.site.register(User,UserAdmin) # table.model , customized model
admin.site.register(Category,CategoryAdmin)
#youmna
admin.site.register(Tag,TagAdmin)
#omar
admin.site.register(Post,PostAdmin)
#samah
admin.site.register(Postlike,PostlikeAdmin)
#rehab
admin.site.register(Word,WordAdmin)
#sandra
admin.site.register(Comment,CommentAdmin)