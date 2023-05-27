from .views import BookingViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include


urlpatterns = [
    path("bookings/", BookingViewset.as_view({"get": "list", "post": "create"})),
    path("bookings/<int:id>/", BookingViewset.as_view({"get": "retrieve"})),
]
