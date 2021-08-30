
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('lender/', views.lenderListView.as_view()),
    path('lender/<int:pk>/', views.lenderDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)