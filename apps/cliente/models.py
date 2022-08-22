from django.db import models
# Create your models here.

class TipoCliente(models.Model):
    customer_type_id = models.AutoField(primary_key=True)
    type_name = models.TextField(unique=True)
    debit_card = models.TextField()
    credit_card = models.TextField()
    current_account = models.TextField()
    checkbook_amount = models.IntegerField()
    box_dollar = models.TextField(blank=True, null=True)
    box_peso = models.TextField(blank=True, null=True)
    withdraw_daily_max = models.IntegerField(blank=True, null=True)
    transfer_comission = models.IntegerField(blank=True, null=True)
    max_travel_reception = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_cliente'

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    customer_type = models.ForeignKey(TipoCliente, models.DO_NOTHING, blank=True, null=True)
    customer_address_id = models.IntegerField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
        

class Direccion(models.Model):
    address_id = models.AutoField(primary_key=True)
    street = models.TextField()
    number = models.IntegerField()
    city = models.TextField()
    province = models.TextField()
    country = models.TextField()

    class Meta:
        managed = False
        db_table = 'direccion'