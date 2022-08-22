from django.db import models

# Create your models here.
class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    balance = models.IntegerField()
    iban = models.CharField(max_length=55)
    account_type = models.TextField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.account_id
    class Meta:
        managed = False
        db_table = 'cuenta'