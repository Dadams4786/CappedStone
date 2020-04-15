from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  image = models.ImageField(upload_to='profile_images/', null=True, blank=True)


  def __str__(self):
    return self.username

class Favorite(models.Model):
  user = models.ForeignKey(User, on_delete=models.PROTECT)
  is_fav = models.BooleanField(default=False)
  title = models.CharField(max_length=100)
  # image = models.CharField(max_length=300)
  instructions = models.CharField(max_length=500)
  ingredients = models.CharField(max_length=500)
  
  def __str__(self):
    return self.user.username + ' ' + self.title