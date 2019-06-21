from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.IntegerField()
    info = models.CharField(max_length=30)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(choices=gender_choice, max_length=6)
    image = models.ImageField(upload_to="images/", blank=True)
    date_added = models.DateTimeField(default=datetime.now) 

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']