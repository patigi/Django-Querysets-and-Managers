from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=200)
    uuid = models.CharField(max_length=20)
	objects = models.Manager()
	public = ActiveLinkManager()
