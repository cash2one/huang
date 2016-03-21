import datetime

from django.test import TestCase

from query.models import Business, Customer


# Create your tests here.
business = Business()
business.type=2
business.money=1
business.customer=Customer.objects.get(id=1)
business.business_time=datetime.datetime.now()
business.save()