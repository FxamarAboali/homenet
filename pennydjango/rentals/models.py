from django.contrib.auth import get_user_model
from django.db import models

from penny.model_utils import BaseModel


class RentProperty(BaseModel):
    publisher = models.ForeignKey(get_user_model(),
                                  related_name="rent_properties",
                                  on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    contact = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    # pictures = NOIDEA
    about = models.TextField(max_length=512, blank=True, null=True)

    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    pets_allowed = models.BooleanField(default=True)

    amenities = models.TextField()
