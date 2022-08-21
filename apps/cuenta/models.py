from django.db import models

# Create your models here.
class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.TextField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'