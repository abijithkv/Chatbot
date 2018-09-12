# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from tgpi.models import Greet
from tgpi.models import Resp
from tgpi.models import B_y_e
# from tgpi.models import Order
from tgpi.models import Purchase


class GrtAdmin(admin.ModelAdmin):
    fields = ['greetings']
    list_display = ['greetings']


class RspAdmin(admin.ModelAdmin):
    fields = ['rsp', 'tag']
    list_display = ['rsp', 'tag']


class ByeAdmin(admin.ModelAdmin):
    fields = ['bye']
    list_display = ['bye']


# class OrderAdmin(admin.ModelAdmin):
#     fields = []


class PurchaseAdmin(admin.ModelAdmin):
    fields = ['pro_query']
    list_display = ['pro_query']


admin.site.register(Greet, GrtAdmin)
admin.site.register(Resp, RspAdmin)
admin.site.register(B_y_e, ByeAdmin)
admin.site.register(Purchase, PurchaseAdmin)