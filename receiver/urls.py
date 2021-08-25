
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('receiver/<str:transactor>/', views.ReceiverDetails.as_view()),
    path('receiver', views.ReceiverListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)