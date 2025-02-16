"""paymeback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

from django.conf.urls import url
from rest_framework.documentation import  include_docs_urls
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('my_lender.urls')),
    path('',include('my_borrower.urls')), 
    path('',include('account.urls')),
    path('',include('transaction.urls')),
    path('docs/',include_docs_urls(title = 'PaymebackAPI')),
    path('', get_schema_view(
        title="Paymeback",
        description="Paymeback APIs",
        version="1.0.0"),name='openapi-schema'
        ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documents_root = settings.MEDIA_ROOT)