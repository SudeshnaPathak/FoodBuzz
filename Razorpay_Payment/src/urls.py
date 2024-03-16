
from django.urls import path, include
from .views import success, home, view

urlpatterns = [
   path('', view, name='view'),
   path('success/', success, name='success'),
   path('payment/', home, name='home')
]