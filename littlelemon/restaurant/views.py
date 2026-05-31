from datetime import date

from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


def index(request):
    return render(request, 'index.html', {'current_year': date.today().year})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
