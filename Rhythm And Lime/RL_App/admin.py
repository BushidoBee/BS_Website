from django.contrib import admin
from .RL_DBMod import Product, Account, Review, RentalOrder

# Main Database classes for viewing information
class AccountsAdmin(admin.ModelAdmin):
    list_display = ['User_id', 'First_Name', 'Last_Name', 'Email', 'Phone_Number', 'Password']
    search_fields = ['User_id']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['Product_Name', 'Product_Type', 'Product_id', 'Price', 'Product_Description', 'Available']
    search_fields = ['Product_Type']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['Review_id', 'Cust_Name', 'Details', 'Rating', 'RVW_TS']
    search_fields = ['Cust_Name']

class RentalOrderAdmin(admin.ModelAdmin):
    list_display = ['Package', 'Cus_id', 'Rental_Number', 'Location', 'Target_Date', 'Completed']
    search_fields = ['Completed']


# Registered Database Models
admin.site.register(Account, AccountsAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(RentalOrder, RentalOrderAdmin)

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