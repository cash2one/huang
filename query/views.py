# -*- coding: utf-8 -*-s
from django.shortcuts import render

from query.models import BusinessMan, Business


# Create your views here.
def index(request):
    business_men = BusinessMan.objects.all()
    return render(request, 'index.html', locals())


def detail(request,bid):
    business_man = BusinessMan.objects.get(id=bid)
    business = Business.objects.filter(business_man=business_man).order_by('business_time')
    return render(request, 'business_detail.html', locals())
