from django.urls import path
from atomicdesigndemo import views

urlpatterns = [
  path('', views.home, name='home'),
  path('home', views.home, name='home'),
  path('help', views.help, name='help'),
  path('bewohnerparkausweis', views.bewohnerparkausweis, name='bewohnerparkausweis'),
  path('ehrenamtskarte', views.ehrenamtskarte, name='ehrenamtskarte'),
]