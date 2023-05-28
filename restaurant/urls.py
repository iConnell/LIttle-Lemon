from .views import BookingViewset, MenuItemViewset
from django.urls import path


urlpatterns = [
    path("bookings/", BookingViewset.as_view({"get": "list", "post": "create"})),
    path("bookings/<int:id>/", BookingViewset.as_view({"get": "retrieve"})),
    path("menu/", MenuItemViewset.as_view({"get": "list"})),
]
