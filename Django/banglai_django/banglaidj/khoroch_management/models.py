from django.db import models

# Create your models here.


class Expenses(models.Model):
    amount = models.IntegerField()
    purpose = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)