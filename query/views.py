# -*- coding: utf-8 -*-s
from django.shortcuts import render

from query.models import BusinessMan, Business, Customer
import traceback,datetime
from django.http.response import HttpResponseRedirect

# Create your views here.
def index(request):
    business_men = BusinessMan.objects.all()
    return render(request, 'index.html', locals())


def detail(request,bid):
    business_man = BusinessMan.objects.get(id=bid)
    business = Business.objects.filter(business_man=business_man).order_by('business_time')
    return render(request, 'business_detail.html', locals())


def add_business(request):
    if request.method == "GET":
        all_customer = Customer.objects.all()
        return render(request, 'add_business.html', locals())
    if request.method == "POST":
        try:
            customer = Customer.objects.get(id=int(request.POST.get('customer_id')))
            business_type = int(request.POST.get('business_type'))
            money = float(request.POST.get('amount'))
            Business.objects.create(type=business_type,money=money,customer=customer,business_time=datetime.datetime.now())
            business_men = BusinessMan.objects.all()
            return HttpResponseRedirect("/")
        except:
            traceback.print_exc()
            return render(request, 'add_err.html', locals())


def add_customer(request):
    if request.method == "GET":
        all_business_man = BusinessMan.objects.all()
        return render(request, 'add_customer.html', locals())
    if request.method == "POST":
        try:
            customer_name = request.POST.get('customer_name')
            try:
                Customer.objects.get(name=customer_name)
                return render(request, 'add_err.html', locals())
            except Customer.DoesNotExist:
                business_man_id = request.POST.get('business_man_id')
                business_man = BusinessMan.objects.get(id=business_man_id)
                Customer.objects.create(name=customer_name,business_man=business_man)
                return HttpResponseRedirect("/")
        except:
            traceback.print_exc()
            return render(request, 'add_err.html', locals())