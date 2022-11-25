from django.shortcuts import render
from plans.models import Plan
from django.http import HttpResponse


def index(request):   
    plan=Plan(plan_id=1, plan_title='test1', plan_content='content1', plan_desc='desc1', plan_time='today' )
    plan.save()
    return HttpResponse("Hello, world. You're at the polls index.")