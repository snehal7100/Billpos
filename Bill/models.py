# from django.db import models

# class Bill(models.Model):
#     pname = models.CharField(max_length=255)
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     total = models.DecimalField(max_digits=10, decimal_places=2)
#     name = models.CharField(max_length=255)
#     payment_term = models.CharField(max_length=50)
#     bill_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"Bill for {self.name} on {self.bill_date}"
