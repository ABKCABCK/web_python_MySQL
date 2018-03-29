# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

from datetime import datetime
from models import Info


def test(request):
    pass
    
def add(request, a, b):
	sum = int(a) + int(b)
	return HttpResponse( str(sum) )

@csrf_exempt
def login( request ) :
	
	try:
		if request.POST :
			login_data = request.POST
			print login_data
			title = 'Project Test User: %s' % (login_data.get('username', ''))
			content = title
			url = ''
			location = 'taipei'
			created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			Info( title=title, content=content, url=url, location=location, created_at=created_at ).save()
	
		return render( request, 'index.html')

	except Exception as e:
		return HttpResponse( str(e) )
	
	
