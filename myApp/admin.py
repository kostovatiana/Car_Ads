from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Car, Manufacturer
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer", "serial_number", )

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "location",)
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ManufacturerAdmin, self).save_model(request, obj, form, change)


admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
