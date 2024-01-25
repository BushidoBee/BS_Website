from django.db import models
from django.utils.timezone import now
import datetime

# Rental Orders -- Ordering System
class Rental_Orders(models.Model):
    # Fields below cannot be empty
    Rent_Order = models.AutoField(null=False, primary_key=True, editable=False)
    Cus_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=False, editable=False)
    Location = models.TextField(null=False, max_length=50, editable=False)
    Completed = models.BooleanField(null=False)
    Ord_TS = models.TextField(null=False)


# Users Database -- All Users registered at Rhy. & Lime
class Users(models.Model):
    # All fields cannot be empty
    User_id = models.AutoField(null=False, primary_key=True, editable=False)
    User_fname = models.TextField(null=False, max_length=40)
    User_lname = models.TextField(null=False, max_length=40)
    Password = models.TextField(null=False, max_length=15)


# Products -- Consumables and Details
class Products(models.Model):
    Code_type = [(FLAV, 'Flavor'),(CNSM, 'Consumable'),(ASST, 'Machines'),(ADVT, 'Advertisement'),(MISC, 'Other')]
    # Prod_id, Prod_type cannot be empty
    Prod_id = models.AutoField(null=False, primary_key=True, editable=False)
    Prod_type = models.CharField(max_length=4, choices=Code_type, null=False)
    Prod_name = models.TextField(null=False, max_length=30)
    Prod_desc = models.TextField(null=False, max_length=1000)
    Price = models.TextField()
    Available = models.BooleanField(null=False)


# R&L Reviews -- Feedback from Customers
class Reviews(models.Model):
    # All fields cannot be empty
    Review_id = models.AutoField(null=False, primary_key=True, editable=False)
    Cus_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)
    Cus_name = models.TextField(null=False, max_length=40)
    Rating = models.IntegerField(null=False)
    Details = models.TextField(null=False)
    Rvw_TS = models.TextField(null=False)
    ...



#--------------------------------------------------------------------------------------------



# Class CarMake w/ Name and Description Fields
class CarMake(models.Model):
    brand = models.CharField(null=False, max_length=20, primary_key=True)
    descript = models.CharField(max_length=1000)

    def __str__(self):
        return self.brand

# Class CarModel w/ Unique ID, Car Brands, Model, Vehicle Type, and Year Fields
class CarModel(models.Model):
    prod_id = 
    
    def __str__(self):
        return  str(self.dealer_id)

# Class CustomerReviews w/ Unique ID, Customer, and the car they bought, and/or reviewed
class CustomerReview(models.Model):
    review_id = models.AutoField(null=False, primary_key=True, editable=False)
    customer_name = models.TextField(null=False, max_length=40)
    dealer_sale = models.IntegerField(null=False)
    make = models.CharField(null=False, max_length=20)
    model = models.CharField(null=False, max_length=20)
    year = models.DateField(null=False)
    car_sold = models.BooleanField()
    date_of_purchase = models.DateField()
    customer_review = models.TextField()
    submit_timestamp = models.TextField()

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
        return "Dealer name: " + self.full_name
      
# Class DealerReview; Holds Basic Data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, vehicle_make, vehicle_model, vehicle_year, sentiment, dealerID):
        # Fields below cannot be empty
        rent_order = models.AutoField(null=False, primary_key=True, editable=False)
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
