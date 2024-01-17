from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import *
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework.authtoken.models import Token

class PaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pays
        fields = '__all__'
        # depth = 3

class LocaliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localite
        fields = '__all__'
        # depth = 3

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'
        # depth = 3

class PaysageUrbainSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaysageUrbain
        fields = '__all__'
        # depth = 3

class RessourceZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = RessourceZone
        fields = '__all__'
        # depth = 3

class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = '__all__'
        # depth = 3
    
# class FinanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Finance
#         fields = '__all__'
#         # depth = 3
    
# class FinanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Finance
#         fields = '__all__'
#         # depth = 3

class RessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ressource
        fields = '__all__'
        # depth = 3

class FinancementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financement
        fields = '__all__'
        # depth = 3

class InfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infrastructure
        fields = '__all__'
        # depth = 3

class MInfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MInfrastructure
        fields = '__all__'
        # depth = 3

class MinistereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministere
        fields = '__all__'
        # depth = 3

class ODDCibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ODDCible
        fields = '__all__'
        # depth = 3

class PotentialitesDesZonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotentialitesDesZones
        fields = '__all__'
        # depth = 3

class ProblemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Probleme
        fields = '__all__'
        # depth = 3

class ProgrammesDesMinisteresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammesDesMinisteres
        fields = '__all__'
        # depth = 3

class ProvenanceFinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvenanceFinance
        fields = '__all__'
        # depth = 3

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
        # depth = 3

# class RessourceHumainesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RessourceHumaines
#         fields = '__all__'
#         # depth = 3