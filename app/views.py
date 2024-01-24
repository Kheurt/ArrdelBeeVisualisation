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
from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.authentication import get_authorization_header
# from rest_framework_jwt.settings import api_settings

from .paginate import ListModelMixin
# from rest_framework import mixins

from .models import *
from .serializer import *

import os
import random
User = get_user_model()


class FinanceViewset(ModelViewSet):

    serializer_class = FinanceSerializer

    queryset = Finance.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset

class FinancementViewset(ModelViewSet):

    serializer_class = FinancementSerializer

    queryset = Financement.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset

class InfrastructureViewset(ModelViewSet):

    serializer_class = InfrastructureSerializer

    queryset = Infrastructure.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset

class LocaliteViewset(ModelViewSet):

    serializer_class = LocaliteSerializer

    queryset = Localite.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset

class MInfrastructureViewset(ModelViewSet):

    serializer_class = MInfrastructureSerializer

    queryset = MInfrastructure.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset

class MinistereViewset(ModelViewSet):

    serializer_class = MinistereSerializer

    queryset = Ministere.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset

class ODDCibleViewset(ModelViewSet):

    serializer_class = ODDCibleSerializer

    queryset = ODDCible.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset

class PaysViewset(ModelViewSet):

    serializer_class = PaysSerializer

    queryset = Pays.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
        
        # if null is not None:
        #     self.queryset = self.queryset.filter(question = question_id)
            
        return self.queryset

class PaysageUrbainViewset(ModelViewSet):

    serializer_class = PaysageUrbainSerializer

    queryset = PaysageUrbain.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset

class PotentialitesDesZonesViewset(ModelViewSet):

    serializer_class = PotentialitesDesZonesSerializer

    queryset = PotentialitesDesZones.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset

class ProblemeViewset(ModelViewSet):

    serializer_class = ProblemeSerializer

    queryset = Probleme.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset

class ProgrammesDesMinistereViewset(ModelViewSet):

    serializer_class = ProgrammesDesMinisteresSerializer

    queryset = ProgrammesDesMinisteres.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset

class ProvenanceFinanceViewset(ModelViewSet):

    serializer_class = ProvenanceFinanceSerializer

    queryset = ProvenanceFinance.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset

class RegionViewset(ModelViewSet):

    serializer_class = RegionSerializer

    queryset = Region.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset
    
    # def retrieve(self, request, *args, **kwargs):
        
        
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response({
    #         'menu' : [],
    #         'data' : serializer.data
    #         })

class RessourcesViewset(ModelViewSet):

    serializer_class = RessourceSerializer

    queryset = Ressource.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
        # filter by region
        # region_id = self.request.query_params.get('region_id')
        # if region_id is not None:
        #     self.queryset = self.queryset.filter(CodeRegion=region_id)
        
        # add filter for each param in .models.zone
        for param in self.request.query_params:
            if param in self.queryset.model._meta.get_fields():
                self.queryset = self.queryset.filter(**{param: self.request.query_params.get(param)})     
        # add pagination to result
        # page = self.paginate_queryset(self.queryset)
        return self.queryset

class RessourceZoneViewset(ModelViewSet):
    
    serializer_class = RessourceZoneSerializer

    queryset = RessourceZone.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true']

    def get_queryset(self):
            
        return self.queryset


class ZoneViewset(ListModelMixin, ModelViewSet):
    """
    # Use ListModelMixin to paginate the response output
    # with the parameters limit and offset (ex: ?limit=10&offset=2)
    """

    serializer_class = ZoneSerializer

    queryset = Zone.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['entitled','is_true']
    filter_fields = ['entitled','is_true', 'Region', 'Departement', 'Commune', 'Localite', 'Zone']
    # pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        # filter by region
        # region_id = self.request.query_params.get('region_id')
        # if region_id is not None:
        #     self.queryset = self.queryset.filter(CodeRegion=region_id)
        
        # add filter for each param in .models.zone

        # for param in self.request.query_params:
        #     if param in self.queryset.model._meta.get_fields():
        #         self.queryset = self.queryset.filter(**{param: self.request.query_params.get(param)})     
        # add pagination to result

        # page = self.paginate_queryset(self.queryset)

        region = self.request.query_params.get('region')
        departement = self.request.query_params.get('departement')
        commune = self.request.query_params.get('commune')
        localite = self.request.query_params.get('localite')
        zone = self.request.query_params.get('zone')

        if region is not None:
            self.queryset = self.queryset.filter(Region=region)
        if departement is not None:
            self.queryset = self.queryset.filter(Departement=departement)
        if commune is not None:
            self.queryset = self.queryset.filter(Commune=commune)
        if localite is not None:
            self.queryset = self.queryset.filter(Localite=localite)
        if zone is not None:
            self.queryset = self.queryset.filter(Zone=zone)
        
        return self.queryset
