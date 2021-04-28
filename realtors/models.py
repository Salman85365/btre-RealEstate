from django.db import models
from datetime import datetime
class Realtor(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to= 'photos/%Y/%m/%d')
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    description = models.TextField(max_length=500, blank=True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name
    
