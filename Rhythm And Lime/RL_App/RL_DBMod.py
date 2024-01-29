from django.db import models
from django.utils.timezone import now
# from django_cryptography.fields import * # working on package installation
import datetime


# Users Database -- All Users registered at Rhy. & Lime
class Account(models.Model):
    # All fields cannot be empty
    User_id = models.AutoField(null=False, primary_key=True, editable=False)
    First_Name = models.CharField(null=False, max_length=40)
    Last_Name = models.CharField(null=False, max_length=40)
    Phone_Number = models.CharField(null=False, max_length=40)
    Email = models.EmailField(null=False, max_length=30)
    Password = models.CharField(max_length=15)

    def __str__(self):
        return "User #" + str(self.User_id)


# Products -- All Products and Descriptions
class Product(models.Model):
    Code_type = [('Flavor', 'FLAV'), ('Consumable','CNSM'), ('Asset','ASST'), ('Advertisement','ADVT'), ('Miscellaneous','MISC')]
    # Product_id, Product_type cannot be empty
    Product_id = models.AutoField(null=False, primary_key=True, editable=False)
    Product_Type = models.CharField(max_length=15,choices=Code_type, null=False)
    Product_Name = models.CharField(null=False, max_length=25)
    Product_Description = models.TextField(null=False, max_length=1000)
    Price = models.DecimalField(max_length=10, default=0, decimal_places=2, max_digits=6)
    Available = models.BooleanField(null=False)
# create foreign key to order_details, rental tables

    def __str__(self):
        return str(Product_Type) + " #" + str(self.Product_id) + ": " + str(Product_Name)


# Rhythm & Lime Reviews -- Feedback from Customers
class Review(models.Model):
    Time_Signature = now() # Submitted Review Timestamp
    # All fields cannot be empty
    Review_id = models.AutoField(null=False, primary_key=True, editable=False)
    Cust_Id = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    Cust_Name = models.CharField(null=False, max_length=40)
    Rating = models.IntegerField(null=False, editable=False)
    Details = models.TextField(null=False, editable=False)
    RVW_TS = models.CharField(max_length=25, null=False, editable=False, default=Time_Signature)


# Order Details -- All items requested within Package Selected
class Cus_Order(models.Model):
    Order_Number = models.AutoField(primary_key=True, on_delete=models.CASCADE, null=False, editable=False)  #to be continued
    Customer = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)


# Rental Orders -- Ordering System
class RentalOrder(models.Model):
    Package_Options = [('STDR','Standard'), ('DELX','Deluxe'), ('PREM','Premium'), ('SPEC','Platinum')]
    # Fields below cannot be empty
    Rental_Num = models.AutoField(primary_key=True, on_delete=models.CASCADE, null=False, editable=False)
    Order_Number = models.ForeignKey(Cus_Order, primary_key=True, on_delete=models.CASCADE, null=False)
    Cus_id = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    Package = models.CharField(max_length=10, choices=Package_Options, default='N/A', null=False)
    Primary = models.ForeignKey(Product.Product_Name, on_delete=models.CASCADE, null=False)
    Secondary = models.ForeignKey(Product.Product_Name, on_delete=models.CASCADE, null=False)
    Location = models.CharField(null=False, max_length=50, default='N/A')
    Target_Date = models.DateField()
    Ord_TS = models.CharField(max_length=25, null=False, editable=False, default='N/A')
    Completed = models.BooleanField(null=False, default=False)


# Items requested within Customer's Order
class Items(models.Model):
    Prod_Type = models.ForeignKey(Product.Product_Type, null=False)
    Order_Items = models.ForeignKey(Product.Product_Name, on_delete=models.CASCADE, null=False)
    Quantity = models.IntegerField(default=0)
    # make a in-line style to OrderDetails Table

#--------------------------------------------------------------------------------------------
# Test Environment


# Class CarMake w/ Name and Description Fields
class CarMake(models.Model):
    brand = models.CharField(null=False, max_length=20, primary_key=True)
    descript = models.CharField(max_length=1000)

    def __str__(self):
        return self.brand

# Class CarModel w/ Unique ID, Car Brands, Model, Vehicle Type, and Year Fields
class CarModel(models.Model):
    pass
    
    def __str__(self):
        return  str(self.dealer_id)


# Class CarDealer; Holds Basic Data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip
    
    def __str__(self):
        return "Unknown: " + self.full_name
      
# Class DealerReview; Holds Basic Data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, vehicle_make, vehicle_model, vehicle_year, sentiment, dealerID):
        # Fields below cannot be empty
        # rent_order = models.AutoField(null=False, primary_key=True, editable=False)
        self.id = id
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        # These fields can be null
        self.purchase_date = purchase_date
        self.purchase_make = vehicle_make
        self.purchase_model = vehicle_model
        self.purchase_year = vehicle_year
        self.sentiment = sentiment

    def __str__(self):
        return "Review: " + self.review

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
