from django.contrib import admin

# Register your models here.
from .models import Member, Item

admin.site.register(Member)
#admin.site.register(Item)

# Define the admin class
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'inventory')

# Register the admin class with the associated model
admin.site.register(Item, ItemAdmin)
