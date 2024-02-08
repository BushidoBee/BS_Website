"""
URL configuration for RL_App project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import process

APP_NAME = 'RL_App'

urlpatterns = [
    path('supersecretRLDB/', admin.site.urls),

     # Home (Index) Page
    path(route='', view=process.homepage, name='index'),

    # About Us; Contact Information
    # path(route='...', view=process.contact, name='About'),

    # Current (Active) Ordering
    # path(route='...', view=process.order_rental, name='Ordering'),

    # Submit Orders/Rentals
    # path(route='...', view=process.submit_rental, name='Rentals'),

    # Account Creation view
    # path(route='...', view=process.accounts, name='Accounts'),

    # Social Media view
    # path(route='...', view=process.socmedia, name='Social'),

    # path for Login/Log-Out
    # path(route='login_logout', view=process.login_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
