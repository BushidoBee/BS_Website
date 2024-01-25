from django.contrib import admin
from .RL_BDMod import Rental_Orders, Users, Products, Reviews





























# Registered Database Models
admin.site.register(Products)
admin.site.register(Users)
admin.site.register(Reviews)
admin.site.register(Rental_Orders)

#----------------------------------------------------------------------------------------------
# References 

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel

# CustomeReviewsAdmin class
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ['review_id', 'customer_name', 'make', 'model', 'year', 'customer_review', 'date_of_purchase']
    search_fields = ['customer_name']

#  CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['car_brand', 'car_model', 'dealer_id', 'vehicle_type', 'year']
    search_fields = ['car_brand']
    EXTRA = 5

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['brand', 'descript']
    search_fields = ['brand']

# Register models here
admin.site.register(Products, CustomerReviewAdmin)
admin.site.register(Users, CarMakeAdmin)
admin.site.register(Reviews, CarModelAdmin)
admin.site.register(Rental_Orders, CarModelAdmin)
