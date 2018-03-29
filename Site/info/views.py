# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime

def test(request):
    return render(request, 'test.html', {
        'current_time': str(datetime.now()),
    })

def add(request, a, b):
	sum = int(a) + int(b)
	return HttpResponse( str(sum) )

def login( request ) :
	return render( request, 'index.html')


