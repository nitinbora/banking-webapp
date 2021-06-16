from django.shortcuts import render
from django.http import HttpResponse
from .models import customer

# Create your views here.
def custo(request):
    all_customer = customer.objects.all()
    return render(request,'custo.html',{'customer': all_customer})
def index(request):
    #return HttpResponse("Index")
    return render(request,'index.html')
def profile(request,cusid):
    #return HttpResponse("Index")
    print(cusid)
    cusid1=customer.objects.filter(ac_numer=cusid)
    print(cusid1)
    return render(request,'profile.html',{'product':cusid1[0]})

def transfer(request,cusid,amount):
    context = {}
    cusid1=customer.objects.filter(ac_numer=cusid)
    context['cusid'] = cusid1[0]
    context['amount'] = amount
    return render(request, 'transfer.html', context=context)
    #return render(request,'transfer.html')
    
def window(request):
    data=customer.objects.all() 
    return render(request,'window.html')
