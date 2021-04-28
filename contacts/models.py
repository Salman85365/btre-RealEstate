from django.db import models
from datetime import datetime

# Create your models here.
class contact(models.Model):
    listing= models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone = models.IntegerField(blank=True)
    user_id= models.IntegerField(blank=True)
    listing_id=models.IntegerField()
    message=models.TextField(blank=True)
    contact_date=models.DateTimeField(default=datetime.now ,blank=True)
    def __str__(self):
        return self.name
    
