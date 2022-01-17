
from django.db import models

from account.models import MyUser


class Order(models.Model):
    guest = models.ForeignKey(MyUser(), on_delete=models.CASCADE, related_name='order')
    # hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel')
    # guesthouse = models.ForeignKey(GuestHouse, on_delete=models.CASCADE, related_name='guesthouse')
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    notes = models.CharField(max_length=300, blank=True)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    arrival_date = models.DateTimeField(auto_now_add=True)
    departure_date = models.DateTimeField(auto_now_add=True)
    quantity_stay = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
