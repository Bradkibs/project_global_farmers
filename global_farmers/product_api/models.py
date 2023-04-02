from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from auth_api.models import User
import uuid


class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, editable=True, blank=False)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(100), MaxValueValidator(10_000)], help_text='Please enter the quantity in Kgs from 100kg to 10 tonnes')
    price = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000_000)], help_text='Please enter the price per kg of the product you are trying to sell!')
    description = models.CharField(max_length=250, help_text='Describe your product shortly', blank=True)
    user_product_table = models.ManyToManyField(User)
