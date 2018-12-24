from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	# body = models.TextField()
	body = MDTextField()

	pub_date = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-pub_date',)

		def __unicode__(self):
			return self.title