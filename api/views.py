from django.shortcuts import render
from rest_framework import generics
from .serializers import CompanySerializer, ContactSerializer
from .models import Company, Contact
 

# Create your views here.

class CompanyView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ContactView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
