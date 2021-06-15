import json
from random import randrange

from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from config.base import SEED_SIZE
from demo.models import Demo
from demo.models import Product


def index(request):
    response = "Demo view works"

    # demo = Demo.objects.create(name='test', arrf_1d=['a', 'b', 'c', 'd'])

    # demo = Demo.objects.create(name='test', arrf_2d=[[1, 2], [3, 4]])
    # demo = Demo.objects.create(name='test', arrf_2d=[[1, 2, 3], [4,5,6]])

    # jdata = json.dumps(data)

    # print(data)
    # print(jdata)

    # demo = Demo.objects.create(jfield=data)
    # demo = Demo.objects.create(jfield=jdata)

    return HttpResponse(response)


def benchmark(request):
    rand_num = randrange(1, SEED_SIZE+1)

    db_size = Product.objects.all().count()

    # Search for item in name column
    _ = Product.objects.get(name=rand_num)
    name_lookup_time = connection.queries[-1]["time"]

    # Search for item in name_idx column
    _ = Product.objects.get(name_idx=rand_num)
    name_idx_lookup_time = connection.queries[-1]["time"]

    # Search for item in attributes column
    _ = Product.objects.get(attributes__name=str(rand_num))
    attrs_name_time = connection.queries[-1]["time"]

    # Search for item in attributes_idx column
    _ = Product.objects.get(attributes_idx__name=str(rand_num))
    attrs_idx_name_time = connection.queries[-1]["time"]

    # Search for list in attributes column
    _ = Product.objects.get(attributes__values__contains=[rand_num, rand_num+1])
    attrs_vals_time = connection.queries[-1]["time"]

    # Search for list in attributes_idx column
    _ = Product.objects.filter(attributes_idx__values__contains=[rand_num, rand_num+1])[0]
    attrs_idx_vals_time = connection.queries[-1]["time"]

    data = {
      'db_size': db_size,
      'value': rand_num,
      'name': name_lookup_time,
      'name_idx': name_idx_lookup_time,
      'attrs_name': attrs_name_time,
      'attrs_idx_name': attrs_idx_name_time,
      'attrs_vals': attrs_vals_time,
      'attrs_idx_vals': attrs_idx_vals_time
    }

    return render(request, 'index.html', data)
