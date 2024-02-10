from django.contrib import admin
from .RL_DBMod import Account, Flavoring, Product, ItemOrder, RentalBook, Review

# Main Database classes for viewing information
class AccountsAdmin(admin.ModelAdmin):
    list_display = ['User_id', 'First_Name', 'Last_Name', 'Email', 'Phone_Number', 'Password', 'RL_Points']
    search_fields = ['User_id', 'First_Name', 'Last_Name', 'Email', 'Phone_Number']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['Product_Name', 'Product_Type', 'Product_id', 'Price', 'Product_Description', 'Available']
    search_fields = ['Product_Type']
    EXTRA = 4

class RL_ColorsAdmin(admin.ModelAdmin):
    list_display = ['Product_Name', 'Product_Description', 'Image', 'Available']
    search_fields = ['Product_Name', 'Available']

class RequestOrders(admin.ModelAdmin):
    list_display = ['Rental_Num', 'Customer', 'Primary', 'Secondary', 'Cups', 'Rimmer_Paks', 'Salt_Paks']
    search_fields = ['Rental_Num']

class RentalOrderAdmin(admin.ModelAdmin):
    list_display = ['Rental_Request', 'Package', 'Flavor', 'Location', 'Target_Date', 'Total', 'Completed', 'Ord_TS']
    search_fields = ['Rental_Request', 'Package', 'Location', 'Completed', 'Total', 'Ord_TS']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['Review_id', 'Cust_Name', 'Details', 'Rating', 'RVW_TS']
    search_fields = ['Cust_Name']

class MultiProducts(admin.StackedInline):
     model = Product


# Registered Database Models; Include other imported classes from RL_DBMod
admin.site.register(Account, AccountsAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Flavoring, RL_ColorsAdmin)
admin.site.register(ItemOrder, RequestOrders)
admin.site.register(RentalBook, RentalOrderAdmin)
admin.site.register(Review, ReviewAdmin)

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
