# coding:utf-8
from django.shortcuts import render,render_to_response,HttpResponse

# Create your views here.
import  os
from web import models
from django.views.decorators.cache import cache_page
import redis
from zyzh_2 import settings
@cache_page(60*15)
def index(req) :
    ry=models.Personnel.objects.all()

    books=models.Book.objects.select_related().all()
    qzs= models.Qz.objects.select_related().all()
    # for qz in qzs :
    #     print qz.zf.age
#    print qzs.query
    bms=models.Dpartment.objects.select_related().all()
    for bm in bms :
       print bm.personnel_set.all()
  #  print (bms.query)
    # d=models.Dpartment.objects.exclude(personnel__id=0).values()
    # print d.query
  #   dms=models.Personnel.objects.exclude().values()
  #   print dms.query
    blog= models.Blog.objects.get(pk=2)

    return  render_to_response('index.html',{'ry':ry,'books':books,'qzs':qzs,'bms':bms,'blog':blog})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def listing(request):
    contact_list = models.FurnitureType.objects.all()
    paginator = Paginator(contact_list, 1) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)


    print paginator.num_pages
    print paginator.page_range
    return render_to_response('list.html', {"contacts": contacts})
import json
from django.core import serializers

from django.conf import settings
from django.core import cache
def json1(req) :
      flag='成功'
      dic={'x':'x'}
      content=models.FurnitureType.objects.all()
      print content
      return  HttpResponse('json',serializers.serialize(content))

import pickle
def redis_save(req) :
      conn = redis.Redis(host='127.0.0.1', port=6379)
      aa= models.FurnitureType.objects.all().values()
      conn.set('names',pickle.dumps(aa))
      dd= conn.get('name')
      print type(pickle.loads(dd))


      return render_to_response('redis.html',{'name':pickle.loads(dd)
          ,'names':pickle.loads(conn.get('names'))})