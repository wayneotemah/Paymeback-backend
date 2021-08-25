
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('customer/<int:phoneNumber>/', views.CustomerDetails.as_view()),
    path('customer/',views.CustomerListView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)