from django.contrib import admin
from .RL_DBMod import Product, Account, Review, RentalOrder

# Main Database classes for viewing information
class AccountsAdmin(admin.ModelAdmin):
    list_display = ['User_id', 'First_Name', 'Last_Name', 'Password']
    search_fields = ['First_Name', 'Last_Name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['Product_id', 'Product_Type', 'Product_Name', 'Password']
    search_fields = ['First_Name', 'Last_Name']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['User_id', 'First_Name', 'Last_Name', 'Password']
    search_fields = ['First_Name', 'Last_Name']

class RentalOrderAdmin(admin.ModelAdmin):
    list_display = ['User_id', 'First_Name', 'Last_Name', 'Password']
    search_fields = ['First_Name', 'Last_Name']


# Registered Database Models
admin.site.register(Product)
admin.site.register(Account)
admin.site.register(Review)
admin.site.register(RentalOrder)

#----------------------------------------------------------------------------------------------
# References 

# CarModelInline class
class CarModelInline(admin.StackedInline):
#     model = CarModel
    pass

# CustomeReviewsAdmin class
class CustomerReviewAdmin(admin.ModelAdmin):
#    list_display = ['review_id', 'customer_name', 'make', 'model', 'year', 'customer_review', 'date_of_purchase']
#    search_fields = ['customer_name']
    pass

#  CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
#    list_display = ['car_brand', 'car_model', 'dealer_id', 'vehicle_type', 'year']
#    search_fields = ['car_brand']
#    EXTRA = 5
    pass

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
#    inlines = [CarModelInline]
#    list_display = ['brand', 'descript']
#    search_fields = ['brand']
    pass