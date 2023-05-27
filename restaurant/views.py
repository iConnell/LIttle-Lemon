from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BookingSerializer
from .models import Booking

# Create your views here.


class BookingViewset(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
