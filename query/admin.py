from django.contrib import admin

from query.models import BusinessMan,Customer,Business


# Register your models here.
class BusinessManAdmin(admin.ModelAdmin):
    list_display = ('name', 'achievement')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'business_man')

class BusinessAdmin(admin.ModelAdmin):
    list_display = ('type', 'money','customer','business_time','business_man')


# Register your models here.

admin.site.register(BusinessMan, BusinessManAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Business, BusinessAdmin)