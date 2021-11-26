from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.

TIPOS_TASKS = (
    ('Pessoal', ("Pessoal")),
    ('Profissional', ("Profissional")),
    ('Outros', ("Outros"))
       
)

class Task(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title           = models.CharField(max_length=200)
    description     = models.TextField(null=True, blank=True)
    complete        = models.BooleanField(default=False)
    create          = models.DateTimeField(auto_now_add=True)
    date            = models.DateTimeField(auto_now_add=True, blank=True)
    tipo            = models.CharField(max_length=50, choices=TIPOS_TASKS, default="Profissional")
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') 
         
    def __str__(self):
        return f'{self.user.username} Profile'

    
    
    
def __str__(self):
    return self.title

class Meta:
    ordering = ['complete']
    
