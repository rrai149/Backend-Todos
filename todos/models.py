from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.timezone import now as utcnow
class Todo(models.Model):
	todo_text = models.CharField(max_length=200)
	publish_time = models.DateTimeField(default = utcnow())
	update_time = models.DateTimeField(default=utcnow())
	def __str__(self):
		return self.todo_text