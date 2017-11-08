# coding:utf-8
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *





class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time',)

class ZfAdmin(admin.ModelAdmin) :
    list_display = ('name',)
    search_fields = ('name', )
    list_filter = ('name',)
#    ordering = ()
class QzAdmin(admin.ModelAdmin) :
    list_display = ('name',)

class DAdmin(admin.ModelAdmin) :
    list_display = ('name',)
    search_fields = ('name',)

class PDadmin(admin.ModelAdmin) :
    list_display = ('name','number1','gz','dpartment')
    search_fields = ('name','number1','gz')

class AuthorAdmin(admin.ModelAdmin) :
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name','email')

class BookAdmin(admin.ModelAdmin) :
    list_display = ('title',)
    search_fields = ('title',)

class FurnitureTypeAdmin(admin.ModelAdmin) :
    list_display = ('type_name','enable')
    search_fields = ('type_name','enable')

class FurnitureAdmin(admin.ModelAdmin) :
    list_display = ('title','img_file')
    search_fields = ('title',)


import redis
import pickle
class BlogAdmin(admin.ModelAdmin) :
    list_display = ('title',)
    search_fields = ('title',)

    def save_model(self, request, obj, form, change):
        conn = redis.Redis(host='127.0.0.1', port=6379)

        conn.set('name',pickle.dumps(obj))

        obj.user = request.user

        obj.save()


class BlogAdmin1(admin.ModelAdmin) :
    list_display = ('title',)
    search_fields = ('title',)

class FurnitureAdmin1(admin.ModelAdmin) :
    list_display = ('title','img_file')
    search_fields = ('title',)

admin.site.register(Blog1,BlogAdmin1)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Furniture1,FurnitureAdmin1)
admin.site.register(FurnitureType,FurnitureTypeAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Zf, ZfAdmin)
admin.site.register(Qz, QzAdmin)
admin.site.register(Dpartment,DAdmin)
admin.site.register(Personnel,PDadmin)