# Generated by Django 5.0.1 on 2024-01-26 01:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('User_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('First_Name', models.TextField(max_length=40)),
                ('Last_Name', models.TextField(max_length=40)),
                ('Password', models.TextField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('brand', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('descript', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Product_Type', models.CharField(choices=[('Flavor', 'FLAV'), ('Consumable', 'CNSM'), ('Machines', 'ASST'), ('Advertisement', 'ADVT'), ('Other', 'MISC')], max_length=15)),
                ('Product_Name', models.CharField(max_length=25)),
                ('Product_Description', models.TextField(max_length=1000)),
                ('Price', models.CharField(max_length=10)),
                ('Available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RentalOrder',
            fields=[
                ('Rent_Order', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Location', models.CharField(editable=False, max_length=50)),
                ('Completed', models.BooleanField()),
                ('Ord_TS', models.CharField(max_length=25)),
                ('Cus_id', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='RL_App.accounts')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('Review_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Cust_Name', models.CharField(max_length=40)),
                ('Rating', models.IntegerField()),
                ('Details', models.TextField()),
                ('RVW_TS', models.CharField(max_length=25)),
                ('Cust_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RL_App.accounts')),
            ],
        ),
    ]