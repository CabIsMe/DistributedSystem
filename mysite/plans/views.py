from django.shortcuts import render, redirect
from plans.models import Plan
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect


# @csrf_protect
def index(request):   
    
    plans=Plan.objects.using('default').all()
    plans_list=list(plans)
    for i in range(len(plans_list)):
        plans_list[i].save(using='write-only')
    mess='Updated!'
    return render(request, 'index.html', {'plans':plans, "message": mess})

