from django.db import models
from user.models import User  # Assuming User is imported correctly
from django.core.validators import MinValueValidator, MaxValueValidator

class PropertyOwner(models.Model):
    nid = models.CharField(max_length=50,unique=True, primary_key=True)  # Unique identifier for PropertyOwner
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)  # Email should be unique to avoid duplicates

    def __str__(self):
        return self.name


class Property(models.Model):
    owner = models.ForeignKey(
        PropertyOwner,
        on_delete=models.CASCADE,  # Deletes the property if the owner is deleted
        related_name="properties"
    )
    location = models.CharField(max_length=255)
    name = models.CharField(max_length=255,null=True, blank=True)
    id = models.CharField(max_length=50,unique=True, primary_key=True) 
    size = models.FloatField(validators=[MinValueValidator(0.1)])
    property_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.owner} ({self.id})"


class Subscription(models.Model):
    owner = models.ForeignKey(
        PropertyOwner,
        on_delete=models.CASCADE,  # Deletes the subscription if the owner is deleted
        related_name="subscriptions"
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,  # Deletes the subscription if the property is deleted
        related_name="subscriptions"
    )
    amount = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])  # Amount must be non-negative
    start_time = models.DateField()
    end_time = models.DateField()
    plan = models.CharField(max_length=50,null=True, blank=True)    

    def __str__(self):
        return f"Plan: {self.plan} for {self.owner.name}"


class Flat(models.Model):
    flat_no= models.CharField(max_length=50,unique=True, primary_key=True) 
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="flats")
    tenant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="flats")  # Tenant is nullable
    room = models.IntegerField(validators=[MinValueValidator(1)])  # Minimum 1 room
    bath = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])  # Optional bath
    attached_bath = models.IntegerField(default=False,null=True, blank=True)  # Boolean is more appropriate for true/false
    drawing = models.BooleanField(default=False,null=True, blank=True)
    dining = models.BooleanField(default=False,null=True, blank=True)
    size = models.FloatField(validators=[MinValueValidator(0)])  # Size cannot be negative
    rent_amount = models.FloatField(validators=[MinValueValidator(0)])  # Rent cannot be negative
    floor = models.IntegerField(validators=[MinValueValidator(0)])  # Floor must be 0 or positive

    def __str__(self):
        return f"Flat on floor {self.floor} of {self.property}"

class Rent(models.Model):
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        help_text="The flat for which rent is being paid."
    )
    tenant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="The tenant paying the rent."
    )
    
    month = models.IntegerField(
        validators=[
            MinValueValidator(1),  # Minimum value of 1 (January)
            MaxValueValidator(12)  # Maximum value of 12 (December)
        ],
        help_text="Month for which the rent is being paid (1-12)."
    )
    year = models.IntegerField(validators=[MinValueValidator(2000)])  # Optional: Ensure a reasonable year range
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["flat", "tenant", "month"],
                name="unique_rent_per_tenant_per_month"
            )
        ]

    def __str__(self):
        return f"Rent for Flat {self.flat.flat_no} by {self.tenant.nid} for Month {self.month}: {self.flat.rent_amount}"



class MaintenanceRequest(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name="maintenance_requests")
    tenant = models.ForeignKey(User, on_delete=models.CASCADE) 
    issue_description = models.TextField()
    request_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)  # Fixed: Corrected `models.models.BooleanField` typo

    def __str__(self):
        return f"Maintenance request for {self.flat} - {'Resolved' if self.status else 'Pending'}"



class User(models.Model):
    nid = models.CharField(max_length=50, primary_key=True)
    members = models.IntegerField(validators=[MinValueValidator(1)])  # Minimum 1 member
    adults = models.IntegerField(validators=[MinValueValidator(0)],null=True, blank=True)  # Must be non-negative
    women = models.IntegerField(validators=[MinValueValidator(0)],null=True, blank=True)  # Must be non-negative

    def __str__(self):
        return f"User {self.nid} with {self.members} members"


# from django.db import models
# from user.models import User 
# # Create your models here.
# class PropertyOwner(models.Model):
#     nid = models.CharField(max_length=50, primary_key=True)  # Unique identifier for PropertyOwner
#     name = models.CharField(max_length=255)
#     contact_info = models.CharField(max_length=255, null=True, blank=True)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name


# class Property(models.Model):
#     owner = models.ForeignKey(
#         PropertyOwner,
#         on_delete=models.CASCADE,  # Deletes the property if the owner is deleted
#         related_name="properties"
#     )
#     location = models.CharField(max_length=255)
#     size = models.FloatField()
#     property_history = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.location} ({self.size} sqm)"


# class Subscription(models.Model):
#     owner = models.ForeignKey(
#         PropertyOwner,
#         on_delete=models.CASCADE,  # Deletes the subscription if the owner is deleted
#         related_name="subscriptions"
#     )
#     property_id = models.ForeignKey(
#         Property,
#         on_delete=models.CASCADE,  # Deletes the subscription if the property is deleted
#         related_name="subscriptions"
#     )
#     amount = models.FloatField(null=True, blank=True)   
#     plan = models.CharField(max_length=50)
#     start_time = models.DateField()
#     end_time = models.DateField()

#     def __str__(self):
#         return f"Plan: {self.plan} for {self.owner.name}"
    
# class Flat(models.Model):
#     property = models.ForeignKey(Property, on_delete=models.CASCADE)
#     tenant = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)    
#     room = models.IntegerField()
#     bath = models.IntegerField(blank=True, null=True)   
#     attached_bath = models.IntegerField(blank=True, null=True)
#     drawing = models.BooleanField(default=False)
#     dining = models.BooleanField(default=False)
#     size = models.FloatField()
#     rent = models.FloatField()
#     floor = models.IntegerField()

# class MaintenanceRequest(models.Model):
#     flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
#     tenant = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 4})
#     issue_description = models.TextField()
#     request_date = models.DateField(auto_now_add=True)
#     status = models.models.BooleanField( default=False)

