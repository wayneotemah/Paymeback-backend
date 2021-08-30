
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('my_borrower/<int:pk>/', views.borrowerDetails.as_view()),
    path('my_borrower/', views.borrowerListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)