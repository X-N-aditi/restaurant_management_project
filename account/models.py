from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharaField(max_length=15)

    def __str__(self):
        return self.name
