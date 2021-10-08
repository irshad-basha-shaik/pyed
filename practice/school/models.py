from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.IntegerField(default="")

    class Meta:
        db_table = "registration"
