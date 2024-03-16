from django.db import models

# Create your models here.
class Payment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default=None ,blank = True, null = True)
    payment_id = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name