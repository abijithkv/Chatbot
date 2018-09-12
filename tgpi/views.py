# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from tgpi.models import Purchase
from tgpi.models import Greet
from tgpi.models import Resp
from tgpi.models import B_y_e
from rest_framework.decorators import api_view
from django.utils.safestring import mark_safe
from tgpi.serializers import gr_serializer
from tgpi.serializers import rp_serializer
from django.http import HttpResponse
from django.http import JsonResponse
import string
import random
import json


@api_view(["POST"])
def mg_grt(request):
    print("Welcome to Askbot")
    # if request.method == 'GET':
    #     gt = Greet.objects.all()
    #     serializer = gr_serializer(gt, many=True)
    #     return HttpResponse(serializer.data)
    if request.method == 'POST':
        dt_c = request.body.decode('utf-8')
        dt = json.loads(dt_c)
        qq = dt['greetings']
        print(qq)
        word = qq.lower()
        print(word)
        time = datetime.datetime.now().time()
        print(time)
        greet = Greet.objects.filter(greetings=word)
        by = B_y_e.objects.filter(bye=word)
        product_query = Purchase.objects.filter(pro_query=word)
        if greet.exists():
            print(greet)
            # if (time>04:00:00) && (time<12:00:00):
            #     print("Good morning")
            word = string.capwords(word)
            ab = Resp.objects.filter(rsp=word, tag="greets")
            print(ab)
            if ab.count() == 0:
                d = Resp(rsp=word)
                d.save()
            r_val = Resp.objects.values('rsp').filter(tag="greets")
            print(r_val)
            rt = random.choice(r_val)
            print(rt)
            return JsonResponse(json.dumps(rt), status=200, content_type="application/json", safe=False)
        elif by.exists():
            bye = Resp.objects.values('rsp').filter(tag="bye")
            bb_val = random.choice(bye)
            return JsonResponse(json.dumps(bb_val), content_type="application/json", status=200, safe=False)
        elif product_query.exists():
            pr = Resp.objects.values('rsp').filter(tag="order")
            return JsonResponse(json.dumps({'rsp': 'Product details are available at: https://www.jtv.com/'}), status=200, content_type="application/json", safe=False)
        else:
            return JsonResponse(json.dumps({'rsp': 'Sorry...I was not able to get you!!'}), status=400, safe=False)
    else:
        return JsonResponse(json.dumps({'rsp': 'Bad Request!!'}), status=400, safe=False)


@api_view(["POST"])
def gret_grt(request):
    if request.method == 'POST':
        gt_c = request.body.decode('utf-8')
        gt = json.loads(gt_c)
        gg = gt['greetings']
        word = gg.lower()
        get_greet = Greet.objects.filter(greetings=word).values()
        if get_greet.exists():
            return JsonResponse(json.dumps({'message': 'Welcome to Askbot. How can I help you?'}), content_type="application/json", safe=False, status=200)
        else:
            return JsonResponse(json.dumps({'message': 'Bad Request!!'}), status=400, safe=False)
