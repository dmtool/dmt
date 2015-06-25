from django.db import models

class User(models.Model):
	first_name = models.SlugField(max_length=45)
	last_name  = models.SlugField(max_length=45)
	Username   = models.CharField(max_length=45)
	email      = models.EmailField()
