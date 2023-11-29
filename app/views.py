from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.decorators import action, api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.authentication import get_authorization_header
# from rest_framework_jwt.settings import api_settings

from .models import *
from .serializer import *

import os
import random
User = get_user_model()

class CountryViewset(ModelViewSet):

    serializer_class = CountrySerializer

    queryset = Country.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
        
        # if null is not None:
        #     self.queryset = self.queryset.filter(question = question_id)
            
        return self.queryset

class LocalityViewset(ModelViewSet):

    serializer_class = LocalitySerializer

    queryset = Locality.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset


class ZoneViewset(ModelViewSet):

    serializer_class = ZoneSerializer

    queryset = Zone.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset
    
class PaysageUrbainViewset(ModelViewSet):

    serializer_class = PaysageUrbainSerializer

    queryset = PaysageUrbain.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset
    
class RessourceZoneViewset(ModelViewSet):

    serializer_class = RessourceZoneSerializer

    queryset = RessourceZone.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset