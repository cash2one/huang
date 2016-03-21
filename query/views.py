# -*- coding: utf-8 -*-s
from django.shortcuts import render

from query.models import BusinessMan


# Create your views here.
def index(request):
    business_men = BusinessMan.objects.all()
    return render(request, 'index.html', locals())
