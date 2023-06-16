"""
URL configuration for thirstfortravel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from travelapi.views import login_user, register_user, TripView, LocationView, DayView, ActivityView, ItineraryView, PackingView, HotelView, TransportationView, SpendingView, BudgetView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'trips', TripView, 'trip')
router.register(r'locations', LocationView, 'location')
router.register(r'days', DayView, 'day')
router.register(r'activities', ActivityView, 'activity')
router.register(r'itineraries', ItineraryView, 'itinerary')
router.register(r'packinglists', PackingView, 'packinglist')
router.register(r'hotels', HotelView, 'hotel')
router.register(r'transports', TransportationView, 'transport')
router.register(r'budgets', BudgetView, 'budget')
router.register(r'spendings', SpendingView, 'spending')
urlpatterns = [
    path('admin/', admin.site.urls),
     path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]
