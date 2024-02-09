from django.contrib import admin
from .RL_DBMod import Product, Account, Review, RentalOrder, Items # Add new Fields into imports

# Main Database classes for viewing information
class AccountsAdmin(admin.ModelAdmin):
    list_display = ['User_id', 'First_Name', 'Last_Name', 'Email', 'Phone_Number', 'Password', 'RL_Points']
    search_fields = ['User_id', 'First_Name', 'Last_Name', 'Email', 'Phone_Number']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['Product_Name', 'Product_Type', 'Product_id', 'Price', 'Product_Description', 'Available']
    search_fields = ['Product_Type']
    EXTRA = 4

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['Review_id', 'Cust_Name', 'Details', 'Rating', 'RVW_TS']
    search_fields = ['Cust_Name']

class RentalOrderAdmin(admin.ModelAdmin):
    list_display = ['Rental_Num', 'Package', 'Cus_id', 'Location', 'Target_Date', 'Completed', 'Ord_TS']
    search_fields = ['Package', 'Location', 'Completed']

class MultiProducts(admin.StackedInline):
     model = Product


# Registered Database Models; Include other imported classes from RL_DBMod
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
