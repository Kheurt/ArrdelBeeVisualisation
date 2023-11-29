from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import *
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework.authtoken.models import Token

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        # depth = 3

class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
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