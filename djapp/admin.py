#sandra
from django.contrib import admin
from .models import *

# Register your models here.

#REEM
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ['User Details',{'fields':['Username','Password','Email','Isadmin','Isblocked']}], #show on create
    )
    list_display = ('Username','Password','Email','Isadmin','Isblocked') # show users list
    list_filter = ['Username','Email','Isadmin','Isblocked'] # advanced
    search_fields = ['Username','Email','Isadmin','Isblocked'] # advanced
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

#sandra
class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        ['User Details',{'fields':['Text','Post_id','User_id']}], #'Time',
    )
    list_display = ('Text','Post_id','User_id') #'Time',

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


#REEM
admin.site.register(User,UserAdmin) # table.model , customized model
admin.site.register(Category,CategoryAdmin)
#sandra
admin.site.register(Comment,CommentAdmin)
#youmna
admin.site.register(Tag,TagAdmin)
#samah
admin.site.register(Postlike,PostlikeAdmin)
#rehab
admin.site.register(Word,WordAdmin)