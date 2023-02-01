from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    tags = models.CharField(max_length=25)
    image = models.FileField(upload_to='img/')
