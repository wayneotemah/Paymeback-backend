
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('owner', views.OwnerListView.as_view()),
    path('owner/<int:transactor>/', views.OwnerDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)