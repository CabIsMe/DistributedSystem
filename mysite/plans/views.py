from django.shortcuts import render, redirect
from plans.models import Plan
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from django.core import serializers
from django.http.response import JsonResponse


def index(request):   
    
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
        return redirect('/plans')

    for p in plans:
        p.save(using='write-only')
    mess='Updated!'


    # serialized_queryset = serializers.serialize('python', plans)
    return render(request, 'index.html', {'plans':plans, "message": mess})
    # return JsonResponse(serialized_queryset, safe=False) 

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

def edit(request, id):
    plan=Plan.objects.get(id=id)
    plans=Plan.objects.using('default').all()

    if request.method=='POST':
        plan.plan_title=request.POST['planTitle']
        plan.plan_content=request.POST['planContent']
        plan.plan_desc=request.POST['planDescription']
        plan.plan_time=request.POST['planTime']
        plan.save()
        return redirect('/plans')
    return render(request, 'index.html', {'plans':plans, 'id': id}) 
        
def delete(request, id):
    plan=Plan.objects.get(id=id)
    plan.delete()
    return redirect('/plans')

