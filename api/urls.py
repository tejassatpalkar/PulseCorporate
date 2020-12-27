from django.urls import path
from .views import CompanyView, ContactView

urlpatterns = [   
    path('', CompanyView.as_view()),
    path('contact/', ContactView.as_view())
]