from django.shortcuts import render,HttpResponse,redirect
from employee_app.models import Employee_details
from django.db.models import Q 

# Create your views here.
def index(request):
    context={}
    e=Employee_details.objects.filter(is_active=True).order_by('-id')
    context['employee']=e
    return render(request,'index.html',context)

def create(request):
    if request.method=='POST':
        uname=request.POST['uname']
        uemail=request.POST['email']
        uage=request.POST['uage']
        address=request.POST['address']
        gender=request.POST['gender']
       
        
        m=Employee_details.objects.create(name=uname,email=uemail,age=uage,address=address,gender=gender)
        m.save()
        return redirect('/')
    else:
        return render(request,'create.html')  
    
def emp_details(request,eid):
    context={}
    q1=Q(is_active=True)
    q2=Q(id=eid)
    e=Employee_details.objects.get(q1 & q2)
    context['emp']=e
    return render(request,'emp_details.html',context)

def delete(request,rid):
    #print("Id to be deleted"+rid)
    d=Employee_details.objects.filter(id=rid)
    d.delete()
    return redirect('/')
    

def edit(request,rid):
    if request.method=='POST':
        
        uname=request.POST['uname']
        uemail=request.POST['email']
        uage=request.POST['uage']
        address=request.POST['address']
        gender=request.POST['gender']
          
        
        u=Employee_details.objects.filter(id=rid) 
        u.update(name=uname,email=uemail,age=uage,address=address,gender=gender)
        
        # return HttpResponse("cfchchg")
        return redirect('/')
        
    else:
        
        emp=Employee_details.objects.get(id=rid)        
        context={}
        context['e']=emp
        return render(request,'edit_emp.html',context)
