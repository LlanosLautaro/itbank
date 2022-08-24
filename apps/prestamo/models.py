from django.db import models

# Create your models here.
class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return 'ID :'+ str(self.loan_id)+'||'+'Fecha: '+str(self.loan_date)+'||'+'Tipo :'+self.loan_type
    class Meta:
        managed = False
        db_table = 'prestamo'