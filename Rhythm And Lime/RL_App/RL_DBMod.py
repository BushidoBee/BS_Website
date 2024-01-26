from django.db import models
from django.utils.timezone import now
import datetime


# Users Database -- All Users registered at Rhy. & Lime
class Account(models.Model):
    # All fields cannot be empty
    User_id = models.AutoField(null=False, primary_key=True, editable=False)
    First_Name = models.CharField(null=False, max_length=40)
    Last_Name = models.CharField(null=False, max_length=40)
    Phone_Number = models.CharField(null=False, max_length=40)
    Email = models.EmailField(null=False, max_length=30)
    Password = models.CharField(null=False, max_length=15)


# Products -- All Products and Descriptions
class Product(models.Model):
    Code_type = ['FLAV', 'CNSM', 'ASST', 'ADVT', 'MISC']
    # Product_id, Product_type cannot be empty
    Product_id = models.AutoField(null=False, primary_key=True, editable=False)
    Product_Type = models.CharField(max_length=15, choices=Code_type, null=False)
    Product_Name = models.CharField(null=False, max_length=25)
    Product_Description = models.TextField(null=False, max_length=1000)
    Price = models.FloatField(max_length=10)
    Available = models.BooleanField(null=False)


# Rhythm & Lime Reviews -- Feedback from Customers
class Review(models.Model):
    # All fields cannot be empty
    Review_id = models.AutoField(null=False, primary_key=True, editable=False)
    Cust_Id = models.ForeignKey(Account.User_id, on_delete=models.CASCADE, null=False)
    Cust_Name = models.CharField(null=False, max_length=40)
    Rating = models.IntegerField(null=False, editable=False)
    Details = models.TextField(null=False, editable=False)
    RVW_TS = models.CharField(max_length=25, null=False, editable=False)



# Rental Orders -- Ordering System
class RentalOrder(models.Model):
    # Fields below cannot be empty
    Rental_Number = models.AutoField(null=False, primary_key=True, editable=False)
    Cus_id = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, editable=False)
    Location = models.CharField(null=False, max_length=50, editable=False)
    Target_Date = models.DateField()
    Ord_TS = models.CharField(max_length=25, null=False, editable=False)
    Completed = models.BooleanField(null=False)


# Order Details -- All items requested within Package Selected
class OrderDetail(models.Model):
    Package_Options = ['Standard', 'Deluxe', 'Premium', 'Platinum']
    Rent_Order = models.ForeignKey(RentalOrder.Rental_Number, null=False, editable=False)
    Packages = models.CharField(max_length=10, choices=Package_Options, null=False)
    Primary_Flavor = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    Secondary_Flavor = models.ForeignKey(Product, on_delete=models.CASCADE, default = 'N/A') #to be continued
#--------------------------------------------------------------------------------------------



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
