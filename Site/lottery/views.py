# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from django.utils import timezone
from models import LottreyNums
# Create your views here.

from datetime import datetime

@csrf_exempt
def index( request ) :

	print timezone.now()

	dataLoad = {
		'number_of_balls': 10,
		'number_can_select': 6
	}
	
	if request.is_ajax() :
		if request.POST :
			post = request.POST
			print post

			user = 'kobe'
			numlist = post.getlist('nums[]')
			assert len(numlist) == dataLoad.get( 'number_can_select', 0 )
			print post['date']
			LottreyNums( date=post['date'], user=user, num_1=numlist[0], num_2=numlist[1], num_3=numlist[2], num_4=numlist[3], num_5=numlist[4], num_6=numlist[5] ).save()

			return JsonResponse( post )

		else :
			print 'No Post Data'

	return render( request, 'index.html', dataLoad )