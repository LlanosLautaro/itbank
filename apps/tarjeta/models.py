from django.db import models

# Create your models here.

class MarcaTarjeta(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=55)

    
    class Meta:
        managed = False
        db_table = 'marca_tarjeta'
    def __str__(self):
        return self.brand_name

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    number_card = models.CharField(unique=True, max_length=200)
    cvv = models.IntegerField()
    issue_date = models.DateField()
    exp_date = models.DateField()
    type_card = models.CharField(max_length=55)
    customer_id = models.IntegerField()
    brand = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarjeta'
        def __str__(self):
            return str(self.customer_id) + '||' + str(self.card_id)+ '-' + str(self.type_card)
class TipoCliente(models.Model):
    customer_type_id = models.AutoField(primary_key=True)
    type_name = models.TextField(unique=True)
    debit_card = models.CharField(max_length=55)
    credit_card =models.CharField(max_length=55)
    current_account = models.CharField(max_length=55)
    checkbook_amount = models.IntegerField()
    box_dollar = models.TextField(blank=True, null=True)
    box_peso = models.TextField(blank=True, null=True)
    withdraw_daily_max = models.IntegerField(blank=True, null=True)
    transfer_comission = models.IntegerField(blank=True, null=True)
    max_travel_reception = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.type_name
    class Meta:
        managed = False
        db_table = 'tipo_cliente'
