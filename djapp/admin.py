#sandra
from django.contrib import admin
from .models import *

#sandra
class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        ['User Details',{'fields':['Text','Post_id','User_id']}], #'Time',
    )
    list_display = ('Text','Post_id','User_id') #'Time',

#sandra
admin.site.register(Comment,CommentAdmin)