
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('accounts/<int:pk>/', views.accountDetails.as_view()),
    path('accounts/',views.accountListView.as_view()),
    path('login',obtain_auth_token, name="login")
]

urlpatterns = format_suffix_patterns(urlpatterns)