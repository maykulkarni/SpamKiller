from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MailTable(models.Model):
	mid = models.IntegerField(primary_key=True)
	sender = models.CharField(max_length = 200)
	subject = models.TextField()
	mail = models.TextField()
	category = models.CharField(max_length=100)
	classification = models.CharField(max_length=100)