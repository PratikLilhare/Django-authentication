from django.db import models

# Create your models here.
class info(models.Model):
    name = models.CharField(max_length = 200)
    info = models.TextField()