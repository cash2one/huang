# -*- coding: utf-8 -*-s
from django.db import models

class BusinessMan(models.Model):
    name = models.CharField(max_length=10, verbose_name=u'姓名')
    achievement = models.FloatField(verbose_name=u'业绩')

    class Meta:
        verbose_name = verbose_name_plural = u'业务员'

    def __unicode__(self):
            return self.name


class Customer(models.Model):
    name = models.CharField(max_length=10, verbose_name=u'姓名')
    business_man = models.ForeignKey(BusinessMan, related_name='customer_manager', verbose_name=u'业务员')

    class Meta:
        verbose_name = verbose_name_plural = u'客户'

    def __unicode__(self):
            return self.name


class Business(models.Model):
    TYPE_CHOICES = (
        (1, u'存入'),
        (2, u'支出'),
    )
    type = models.IntegerField(choices=TYPE_CHOICES,verbose_name=u'类型')
    money = models.FloatField(verbose_name=u'金额')
    customer = models.ForeignKey(Customer, related_name='business_customer', verbose_name=u'客户')
    business_time = models.DateTimeField(verbose_name=u'业务时间')
    business_man = models.ForeignKey(BusinessMan, related_name='business_man', verbose_name=u'业务员')

    class Meta:
        verbose_name = verbose_name_plural = u'业务'

    def __unicode__(self):
            return str(self.id)

    def save(self, *args, **kwargs):
        self.business_man = self.customer.business_man
        if self.type==1:
            self.customer.business_man.achievement += self.money
        else:
            self.customer.business_man.achievement -= self.money
        self.customer.business_man.save()
        super(Business, self).save(*args, **kwargs)


