from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class User(models.Model):
    nid = models.CharField(max_length=50, primary_key=True)
    members = models.IntegerField(
        validators=[MinValueValidator(1)],  # Ensure non-negative values
        help_text="Total number of members in the household."
    ) 
    name = models.CharField(max_length=255,null=True, blank=True)
    adults = models.IntegerField(
        null=True,blank=True,
        validators=[MinValueValidator(1)],  # Ensure non-negative values
        help_text="Number of adults in the household."
    )
    women = models.IntegerField(
        null=True,blank=True,
        validators=[MinValueValidator(0)],  # Ensure non-negative values
        help_text="Number of women in the household."
    )

    def __str__(self):
        return f"User {self.nid} with {self.members} members"


# from django.db import models
# from properties.models import Flat
# from django.core.validators import MinValueValidator, MaxValueValidator
# # Create your models here.
# class User(models.Model):
#     nid = models.CharField(max_length=50, primary_key=True)
#     members = models.IntegerField()
#     adults = models.IntegerField()
#     women = models.IntegerField()
    
    
# class Rent(models.Model):
#     flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
#     tenant = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.FloatField()
#     month = models.IntegerField(  validators=[
#             MinValueValidator(1),  # Minimum value of 1
#             MaxValueValidator(12)  # Maximum value of 12
#         ])
    