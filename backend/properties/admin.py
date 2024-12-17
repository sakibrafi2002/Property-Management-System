from django.contrib import admin
from .models import PropertyOwner, Property, Subscription, Flat, Rent, MaintenanceRequest

@admin.register(PropertyOwner)
class PropertyOwnerAdmin(admin.ModelAdmin):
    list_display = ('nid', 'name', 'email', 'contact_info')  # Display fields in admin list view
    search_fields = ('name', 'email', 'nid')  # Enable searching by these fields
    list_filter = ('email',)  # Filter by email

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'location', 'size')  # Display fields in admin list view
    search_fields = ('location',)  # Enable searching by location
    list_filter = ('location',)  # Filter by location

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'property', 'plan', 'start_time', 'end_time', 'amount')
    search_fields = ('owner__name', 'plan')  # Enable searching by owner name or plan
    list_filter = ('start_time', 'end_time', 'plan')  # Add filters for dates and plan

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('flat_no', 'property', 'tenant', 'room', 'bath', 'size', 'rent_amount', 'floor')
    search_fields = ('property__location', 'tenant__nid')  # Enable searching by property location or tenant NID
    list_filter = ('floor', 'size', 'rent_amount')  # Add filters for floor, size, and rent

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('id', 'flat', 'tenant', 'month', 'year')
    search_fields = ('tenant__nid', 'flat__property__location')  # Enable searching by tenant or property location
    list_filter = ('month', 'year')  # Add filters for month and year

@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'flat', 'tenant', 'issue_description', 'request_date', 'status')
    search_fields = ('flat__property__location', 'tenant__nid', 'issue_description')  # Enable searching
    list_filter = ('status', 'request_date')  # Add filters for status and request date
