from django.db import models
from django.contrib.auth.models import Group,User
# Create your models here.

class Timeline(models.Model):
	owner = models.ForeignKey(User)
	owner_name = models.CharField(max_length=32)
	content = models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField(default=0)
	class Meta(object):
		db_table='Timeline'

