# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BaseModel(models.Model):
    name = models.CharField(max_length=32)
    note = models.TextField(null=True, blank=True)
    createtime = models.DateField(null=True, blank=True, auto_now_add = True)
    updatetime = models.DateField(null=True, blank=True, auto_now = True )

    def __unicode__(self): # 在 Python3 用__str__代替__unicode__
        return self.name

    class Meta:
        ordering = ['-id']
        abstract = True



class Book(BaseModel):
    price = models.IntegerField()
    publish = models.ForeignKey("Publish", null=True, blank=True)
    author = models.ManyToManyField("Author", null=True, blank=True)

    @property
    def priceplus(self):
        return self.price + 1

    @property
    def todict(self):
        include = ['name','note']
        ret = dict()
        for attr in self._meta.fields:
            fieldname = attr.name
            fieldvalue = getattr(self, fieldname)
            if fieldname in include:
                if fieldname == 'note':
                    if fieldvalue and len(fieldvalue) > 5:
                        fieldvalue = fieldvalue[0:5] + '... ...'
                ret[fieldname] = fieldvalue
        return ret


class Publish(BaseModel):
    city = models.CharField(max_length=32)


class Author(BaseModel):
    address = models.CharField(max_length = 64, null = True, blank = True)
    phone = models.CharField(max_length = 11, null = True, blank = True)
    fans = models.IntegerField(null = True, blank = True) # integer 类型的一个重要作用是排序, 如粉丝量前几
    income = models.IntegerField(null = True, blank = True)

    @property
    def todict(self):
        include = ['name', 'address', 'phone']
        ret = dict()
        # 正常字段
        for attr in self._meta.fields:
            fieldname = attr.name
            fieldvalue = getattr(self, fieldname)
            if fieldname not in include:continue
            if fieldname == 'phone': # 隐藏中间四位
                if fieldvalue and len(fieldvalue) == 11:
                    fieldvalue = fieldvalue[0:3] + '^_^' + fieldvalue[7:11]
            ret[fieldname] = fieldvalue
        # 关联字段
        ret['books'] = [{"name": book.name, "price": book.price} for book in self.book_set.all()]
        return ret








