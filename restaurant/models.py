from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class MenuItem(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    description = models.TextField(max_length=1000, default="")


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(unique=True)
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        return f"{self.user.first_name} on {self.reservation_date}"
