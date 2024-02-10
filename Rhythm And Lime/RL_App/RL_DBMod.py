from django.db import models
from django.utils.timezone import now
import json
# from django_cryptography.fields import * # working on package installation
import datetime


Time_Signature = now() # Submitted Timestamp

# Users Database -- All Users registered at Rhy. & Lime
class Account(models.Model):
    # All fields cannot be empty
    User_id = models.AutoField(primary_key=True, editable=False)
    First_Name = models.CharField(null=False, max_length=40)
    Last_Name = models.CharField(null=False, max_length=40)
    Phone_Number = models.CharField(null=False, max_length=40)
    Email = models.EmailField(null=False, max_length=30)
    Password = models.CharField(max_length=15)
    RL_Points = models.IntegerField(default=0, editable = False)

    def __str__(self):
        return "User #" + str(self.User_id)

# Margarita Flavors -- All Descriptive Flavors
class Flavoring(models.Model):
    Product_Name = models.CharField(primary_key=True, max_length=25)
    Product_Description = models.TextField(null=False, max_length=400)
    Image = models.ImageField(upload_to="RL_Images/", max_length=100) #Further Edit this Field before Migration 
    Available = models.BooleanField(default=True, null=False)

    def __str__(self):
        return str(self.Product_Name)

# Products -- All Products and Descriptions
class Product(models.Model):
    Code_type = [('CNSM','Consumable'), ('ASST','Asset'),
                 ('ADVT','Advertisement'), ('MISC','Miscellaneous')]
    # Product_id, Product_type cannot be empty
    Product_id = models.AutoField(primary_key=True, editable=False)
    Product_Type = models.CharField(max_length=15, choices=Code_type, null=False)
    Product_Name = models.CharField(null=False, max_length=25)
    Product_Description = models.TextField(null=False, max_length=300)
    Price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    Available = models.BooleanField(default=True, null=False)
# create foreign key to order_details, rental tables

    def __str__(self):
        return str(self.Product_Type) + " #" + str(self.Product_id) + ": " + str(self.Product_Name)

# Items requested within Customer's Order
class ItemOrder(models.Model):
    Color_Code = [('R','Red'), ('B','Blue'), ('G','Green'), ('Y','Yellow'),
                 ('P','Pink'), ('E','Grey'), ('W','White'), ('K','Black')]
    Rental_Num = models.AutoField(primary_key=True, editable=False)
    # Extra Items to add to Order
    Customer = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, default=0)
    Primary = models.CharField(max_length=15, choices=Color_Code, null=False)
    Secondary = models.CharField(max_length=15, choices=Color_Code, null=False, blank=True, default='N/A')
    Cups = models.IntegerField(default=0)
    Rimmer_Paks = models.IntegerField(default=0)
    Salt_Paks = models.IntegerField(default=0)

    def __str__(self):
        return "Order Number: " + str(self.Rental_Num)

# Rental Orders -- Rental Booking for Clients
class RentalBook(models.Model):
    Package_Options = [('STDR','Standard'),
                       ('DELX','Deluxe'),
                       ('PREM','Premium'),
                       ('SPEC','Platinum')]
    # Fields below cannot be empty
    Rental_Request = models.OneToOneField(ItemOrder, unique=True, on_delete=models.CASCADE, null=False)
    Package = models.CharField(max_length=10, choices=Package_Options, default='Standard', null=False)
    Flavor = models.ForeignKey(Flavoring, on_delete=models.CASCADE, null=False)
    Location = models.CharField(null=False, max_length=50, default='N/A')
    Target_Date = models.DateField()
    Total = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    Completed = models.BooleanField(null=False, default=False)
    Ord_TS = models.CharField(max_length=25, null=False, editable=False, default='N/A')

    def __str__(self):
        return "Rental " + str(self.Rental_Request) + " | " + str(self.Package)

# Rhythm & Lime Reviews -- Feedback from Customers
class Review(models.Model):
    Review_Stars = [('None', 0), ('Unsatisfied', 1), ('Poor', 2), ('Average', 3), ('Good', 4), ('Excellent', 5)]
    # All fields cannot be empty
    Review_id = models.AutoField(primary_key=True, editable=False)
    Cust_Id = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    Cust_Name = models.CharField(max_length=40, null=False)
    Rating = models.IntegerField(editable=False, choices = Review_Stars, null=False)
    Details = models.TextField(editable=False, null=False)
    RVW_TS = models.CharField(max_length=25, editable=False, null=False)#, default=Time_Signature)