from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'id')


@admin.register(Customer)
class Customerdata(ImportExportModelAdmin):
  pass
    
@admin.register(Bike)
class Bikedata(ImportExportModelAdmin):
    pass


@admin.register(Rental)
class Rentaldata(ImportExportModelAdmin):
    list_display = ('user', 'bike')
    readonly_fields = ('user', 'bike', 'start_time', 'end_time', 'total_cost')
    
    def get_user_name(self, obj):
        return obj.user.user_name

    get_user_name.short_description = 'User Name'
