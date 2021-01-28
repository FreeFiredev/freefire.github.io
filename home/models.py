from django.db import models

# Create your models here.
class Victim(models.Model):
  uname = models.TextField(max_length=30)
  password = models.TextField(max_length=30)
  joined_date = models.DateField()
  def __str__(self):
    return self.uname
