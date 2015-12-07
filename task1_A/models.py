    # -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('Категория товара', max_length=64)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория')
    name = models.CharField('Наименование товара', max_length=128)
    price = models.DecimalField('Цена единицы, руб.', max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.name, self.price


class Person(models.Model):
	name = models.CharField('Item', max_length=100)
	birthday = models.DateField(null=True, blank=False)




    # Product.objects.filter(price__gte=100)
    # Product.objects.values('category').annotate(cnt=Count('price'))
    # Product.objects.values('category').annotate(cnt=Count('price')).filter(cnt__gt=10)


    # from task1_A.models import Product
    # pp = Product.objects.all()
    # for p in pp:
    # print p.category, p.name, p. price
