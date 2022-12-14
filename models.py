# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
""" from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.AutoField()
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    clave = models.CharField(max_length=4, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.AutoField()
    usuario_id = models.BigIntegerField()
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('usuario_id', 'group'),)


class AuthUserPermissions(models.Model):
    id = models.AutoField()
    usuario_id = models.BigIntegerField()
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_permissions'
        unique_together = (('usuario_id', 'permission'),)


class Cliente(models.Model):
    customer_id = models.AutoField()
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    customer_type = models.ForeignKey('TipoCliente', models.DO_NOTHING, blank=True, null=True)
    customer_address_id = models.IntegerField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField()
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.TextField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'


class Direccion(models.Model):
    address_id = models.AutoField()
    street = models.TextField()
    number = models.IntegerField()
    city = models.TextField()
    province = models.TextField()
    country = models.TextField()

    class Meta:
        managed = False
        db_table = 'direccion'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user_id = models.BigIntegerField()
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    employee_id = models.AutoField()
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()
    employee_address_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class MarcaTarjeta(models.Model):
    brand_id = models.AutoField()
    brand_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'


class Prestamo(models.Model):
    loan_id = models.AutoField()
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField()
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjeta(models.Model):
    card_id = models.AutoField()
    number_card = models.CharField(unique=True, max_length=200)
    cvv = models.IntegerField()
    issue_date = models.TextField()
    exp_date = models.TextField()
    type_card = models.TextField()
    customer_id = models.IntegerField()
    brand = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarjeta'


class TipoCliente(models.Model):
    customer_type_id = models.AutoField()
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
        db_table = 'tipo_cliente' """
