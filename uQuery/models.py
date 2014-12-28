#!/usr/bin/env python
# -*- coding: cp936 -*-

from django.db import models

class UserModel(models.Model):
    time = models.CharField(u'时间', max_length=20)
    fwqName = models.CharField(u'服务器', max_length=10)
    fwqID = models.CharField(u'服务器编号', max_length=5)
    usrID = models.CharField(u'用户ID', max_length=10)
    usrName = models.CharField(u'用户昵称', max_length=20)
    account = models.CharField(u'用户帐号', max_length=100)
    app = models.CharField(u'APP', max_length=20)
    device = models.CharField(u'设备型号', max_length=100)
    udid = models.CharField(u'UDID', max_length=100)
    usrTel = models.CharField(u'手机号码', max_length=20, blank=True)

    def __unicode__(self):
        return u'%s %s, %s %s' % (self.fwqID, self.fwqName, self.usrID, self.usrName)

    class Meta:
        abstract = True

class AllUser(UserModel):
    class Meta:
    	verbose_name = u'所有用户'
        verbose_name_plural = u'所有用户'
