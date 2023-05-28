from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BookingSerializer, MenuItemSerializer
from .models import Booking, MenuItem
from rest_framework.response import Response
from datetime import datetime

# Create your views here.


class BookingViewset(ModelViewSet):
    serializer_class = BookingSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Booking.objects.filter(user=user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, 201)

        return Response(serializer.errors, 400)


class MenuItemViewset(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
