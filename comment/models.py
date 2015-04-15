from django.db import models
from timeline.models import Timeline
# Create your models here.

class Comment(models.Model):
	timeline = models.ForeignKey(Timeline)
	content = models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)

	class Meta(object):
		db_table='Timeline_Comments'
