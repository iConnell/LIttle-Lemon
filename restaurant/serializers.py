from rest_framework import serializers
from .models import Booking, MenuItem


class BookingSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        reservation_time = attrs.get("reservation_date")

        reservation_date_date = reservation_time.date()
        reservation_hour = reservation_time.time().hour

        if Booking.objects.filter(
            reservation_date__time__hour=reservation_hour, reservation_date__date=reservation_date_date
        ).exists():
            raise serializers.ValidationError("This time slot has already been booked")

        return attrs

    class Meta:
        model = Booking
        fields = ["reservation_date", "reservation_slot"]


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"
