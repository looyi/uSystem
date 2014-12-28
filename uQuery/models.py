#!/usr/bin/env python
# -*- coding: cp936 -*-

from django.db import models

class UserModel(models.Model):
    time = models.CharField(u'ʱ��', max_length=20)
    fwqName = models.CharField(u'������', max_length=10)
    fwqID = models.CharField(u'���������', max_length=5)
    usrID = models.CharField(u'�û�ID', max_length=10)
    usrName = models.CharField(u'�û��ǳ�', max_length=20)
    account = models.CharField(u'�û��ʺ�', max_length=100)
    app = models.CharField(u'APP', max_length=20)
    device = models.CharField(u'�豸�ͺ�', max_length=100)
    udid = models.CharField(u'UDID', max_length=100)
    usrTel = models.CharField(u'�ֻ�����', max_length=20, blank=True)

    def __unicode__(self):
        return u'%s %s, %s %s' % (self.fwqID, self.fwqName, self.usrID, self.usrName)

    class Meta:
        abstract = True

class AllUser(UserModel):
    class Meta:
    	verbose_name = u'�����û�'
        verbose_name_plural = u'�����û�'
