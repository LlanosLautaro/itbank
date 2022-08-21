# Generated by Django 4.1 on 2022-08-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarcaTarjeta',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.TextField()),
            ],
            options={
                'db_table': 'marca_tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('card_id', models.AutoField(primary_key=True, serialize=False)),
                ('number_card', models.CharField(max_length=200, unique=True)),
                ('cvv', models.IntegerField()),
                ('issue_date', models.TextField()),
                ('exp_date', models.TextField()),
                ('type_card', models.TextField()),
                ('customer_id', models.IntegerField()),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('customer_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.TextField(unique=True)),
                ('debit_card', models.TextField()),
                ('credit_card', models.TextField()),
                ('current_account', models.TextField()),
                ('checkbook_amount', models.IntegerField()),
                ('box_dollar', models.TextField(blank=True, null=True)),
                ('box_peso', models.TextField(blank=True, null=True)),
                ('withdraw_daily_max', models.IntegerField(blank=True, null=True)),
                ('transfer_comission', models.IntegerField(blank=True, null=True)),
                ('max_travel_reception', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tipo_cliente',
                'managed': False,
            },
        ),
    ]
