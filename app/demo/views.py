import json
from random import randrange

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

from config.base import SEED_SIZE
from demo.models import Demo
from demo.models import Product


def index(request):
    response = "Demo view works"

    # demo = Demo.objects.create(name='test', arrf_1d=['a', 'b', 'c', 'd'])

    # demo = Demo.objects.create(name='test', arrf_2d=[[1, 2], [3, 4]])
    # demo = Demo.objects.create(name='test', arrf_2d=[[1, 2, 3], [4,5,6]])

    # data = [{
    #     "age": 76,
    #     "name": 'Arnold',
    #     "surname": 'Schwarzenegger',
    # },{
    #     "age": 60,
    #     "name": 'Michael',
    #     "surname": 'Fox',
    # }]

    # jdata = json.dumps(data)

    # print(data)
    # print(jdata)

    # demo = Demo.objects.create(jfield=data)
    # demo = Demo.objects.create(jfield=jdata)

    return HttpResponse(response)


def benchmark(request):
    rand_num = randrange(0, SEED_SIZE)
    _ = Product.objects.filter(attributes__name=rand_num).first()

    dict_lookup_time = connection.queries[-1]["time"]

    _ = Product.objects.filter(attributes__values__contains=[rand_num, rand_num+1]).first()

    list_lookup_time = connection.queries[-1]["time"]
    return HttpResponse(
        f"dict lookup time: {dict_lookup_time}"
        "<br/>"
        f"list lookup time: {list_lookup_time}"
    )