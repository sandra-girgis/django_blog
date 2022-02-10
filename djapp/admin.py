#sandra
from django.contrib import admin
from .models import *


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

#rehab
class WordAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Category Details',{'fields':['Name']}],
    )
    list_display = ('Name',)
    search_fields = ['Name']

#sandra
admin.site.register(Comment,CommentAdmin)
#youmna
admin.site.register(Tag,TagAdmin)
#rehab
admin.site.register(Word,WordAdmin)