from django.contrib import admin
from .models import *

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display=['id','name','description']

class TopicAdmin(admin.ModelAdmin):
    list_display=['id','subject','last_update','board','starter']

class PostAdmin(admin.ModelAdmin):
    list_display=['id','message','created_at','updated_at','created_by','updated_by','topic']

admin.site.register(Board,BoardAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Post,PostAdmin)
