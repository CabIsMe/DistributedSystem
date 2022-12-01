from django.shortcuts import render, redirect
from plans.models import Plan
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect


def index(request):   
    plans=Plan.objects.using('default').all()
    for p in plans:
        p.save(using='write-only')
    mess='Updated!'
    return render(request, 'index.html', {'plans':plans, "message": mess})


@csrf_protect
def create(request):
    plans=Plan.objects.using('default').all()
    if request.method == 'POST':
        planId=plans.reverse()[0].plan_id+1
        planTitle=request.POST['planTitle']
        planContent=request.POST['planContent']
        planDesc=request.POST['planDescription']
        planTime=request.POST['planTime']
        
        plan = Plan(plan_id=planId ,plan_title=planTitle, plan_content=planContent, plan_desc=planDesc, plan_time=planTime)
        print(plan)
        plan.save(using='default')
    return render(request, 'create.html')   
        

