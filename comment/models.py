from django.db import models
from timeline.models import Timeline
# Create your models here.

class Comment(models.Model):
	timeline = models.ForeignKey(Timeline)
	comment_user = models.CharField(max_length=32)
	content = models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)

	class Meta(object):
		db_table='Timeline_Comments'
