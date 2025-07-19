from django.db import models

# Create your models here. Database
class Photo(models.Model):
    file = models.FileField(upload_to='file')