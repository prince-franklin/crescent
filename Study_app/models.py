from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Crescentlib(models.Model):
    manager=models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    book=models.CharField(max_length=255)
    read=models.BooleanField(default=False)
    
    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.book
