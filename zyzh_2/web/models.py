# coding:utf-8
from __future__ import unicode_literals

from DjangoUeditor.models import UEditorField

# Create your models here.

from django.db import models


class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '老公'
        verbose_name_plural = '老公'
    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title

class Zf(models.Model) :
    name=models.CharField(u'丈夫名字',max_length=100)
    age=models.IntegerField(u'年龄',)

    def __unicode__(self):
        return self.name

class Qz(models.Model) :
    zf=models.OneToOneField(
        Zf,
        on_delete=models.CASCADE,
        primary_key=True,

    )
    name=models.CharField(u'妻子名字',max_length=100)
    age=models.IntegerField(u'年龄')

    def __unicode__(self):
        return "%s,%s" % (self.name,self.zf.name)

class Dpartment(models.Model) :
    name=models.CharField(u'部门名字',max_length=30)

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门'

    def __unicode__(self):
        return self.name

class Personnel(models.Model) :
    name=models.CharField(u'人员名称',max_length=20)
    number1=models.IntegerField(u'编号')
    gz=models.IntegerField(u'工资')
    dpartment=models.ForeignKey(
        Dpartment,verbose_name='部门'
    )

    class Meta:
        verbose_name = '人员'
        verbose_name_plural = '人员'
    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(u'第一个作者',max_length=30)
    last_name = models.CharField(u'最后一个作者',max_length=40)
    email = models.EmailField()

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'

    def __unicode__(self):
        return self.first_name

class Book(models.Model):
    title = models.CharField(u'书名',max_length=200)
    authors = models.ManyToManyField(Author)

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'

    def __unicode__(self):
        return self.title

class FurnitureType(models.Model) :
    type_name=models.CharField(u'分类名称',max_length=30)
    enable=models.IntegerField(choices=((1,'是'),(0,'否')),default=1,verbose_name='是否启用')

    class Meta:
        verbose_name = '家具分类'
        verbose_name_plural = '家具分类'

    def __unicode__(self):
        return self.type_name



class Furniture(models.Model) :
    title=models.CharField(u'标题',max_length=60)
    img_file=models.ImageField(u'图片',upload_to='/static/imgs')

    class Meta:
        verbose_name = '家具详情'
        verbose_name_plural = '家具详情'

    def __unicode__(self):
        return self.title

class Furniture1(models.Model) :
    title=models.CharField(u'标题',max_length=60)
    img_file=models.ImageField(u'图片',upload_to='/static/imgs')

    class Meta:
        verbose_name = '家具详情'
        verbose_name_plural = '家具详情'

    def __unicode__(self):
        return self.title


class Blog(models.Model) :
    title=models.CharField(u'标题',max_length=200)
    content=UEditorField(u'正文',height=500, width=700,
        default=u'', blank=True,imagePath="static/uploads/images/",
        toolbars='full', filePath='static/uploads/files/')
    add_time=models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)


    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'

    def __unicode__(self):
        return self.title

class Blog1(models.Model) :
    title=models.CharField(u'标题',max_length=200)
    content=UEditorField(u'正文',height=500, width=700,
        default=u'', blank=True,imagePath="static/uploads/images/",
        toolbars='full', filePath='static/uploads/files/')
    add_time=models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '博客1'
        verbose_name_plural = '博客1'

    def __unicode__(self):
        return self.title

