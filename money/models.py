from django.db import models

# Create your models here.
class customer(models.Model):
    customer_id=models.AutoField
    customer_name=models.CharField(max_length=200)
    ac_numer=models.IntegerField()
    balance=models.IntegerField(null=True)
    