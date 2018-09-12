# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class Greet(models.Model):
    greetings = models.CharField(max_length=100)

    def __str__(self):
        return self.greetings


class Resp(models.Model):
    rsp = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.rsp


class Order(models.Model):
    Item_name = models.CharField(max_length=500)
    Item_no = models.CharField(max_length=100)
    Customer_name = models.CharField(max_length=500)
    Distr_name = models.CharField(max_length=500)
    Order_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Item_name, self.Item_no, self.Customer_name, self.Distr_name, self.Order_date


class Purchase(models.Model):
    custo_name = models.CharField(max_length=500)
    Pro_id = models.CharField(max_length=500)
    Pay_amt = models.IntegerField(default=10000)
    pay_id = models.CharField(max_length=500)
    pro_query = models.CharField(max_length=500)

    def __str__(self):
        return self.pro_query


class B_y_e(models.Model):
    bye = models.CharField(max_length=100)

    def __str__(self):
        return self.bye
