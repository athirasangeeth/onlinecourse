import email
from django.db import models

class Registration(models.Model):
    username=models.TextField(max_length=10)
    password=models.TextField(max_length=12)
    email=models.EmailField()
    age=models.IntegerField()

    class Meta:
        db_table='registration'