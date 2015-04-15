#! -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import Group,User

class UserProfile(models.Model):
	owner = models.ForeignKey(User)#所属于的用户
	name = models.CharField(max_length=32)#名称
	tel = models.CharField(max_length=15) #手机
	email = models.CharField(max_length=32) #邮箱
	address = models.CharField(max_length=256) #地址
	remark = models.TextField() #备注
	status = models.BooleanField(default=True) #状态
	created_at = models.DateTimeField(auto_now_add=True) #创建时间
	is_deleted = models.BooleanField(default=False) #是否删除

	class Meta(object):
		db_table = 'User_Profile'
		ordering=['-id']

class Follower_List(models):
	owner=models.ForeignKey(User)
	follower_id=models.IntegerField()#总数库中唯一的id
	follower_name=models.CharField(max_length=32)

	class Meta(object):
		db_table='Friend_List'
		ordering=['-id']