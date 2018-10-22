from django.db import models

# Create your models here.

class UserModel(models.Model):
    FIELDNAME = models.CharField( max_length=50)