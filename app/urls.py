from django.urls import path, include
from .views import CountryViewset, LocalityViewset, RessourceZoneViewset, PaysageUrbainViewset, ZoneViewset
from .upload_data import upload_country, upload_locality, upload_zone, upload_paysage_urbain, upload_ressource_zone

from rest_framework import routers

router = routers.DefaultRouter()
router.register('country', CountryViewset),
router.register('locality', LocalityViewset),
router.register('zone', ZoneViewset),
router.register('paysageUrbain', PaysageUrbainViewset),
router.register('ressourceZone', RessourceZoneViewset),

# Country
# Locality
# Zone
# PaysageUrbain
# RessourceZone

urlpatterns = [
    path('', include(router.urls)), 
    path('country/upload', upload_country),
    path('locality/upload', upload_locality),
    path('zone/upload', upload_zone),
    path('paysageUrbain/upload', upload_paysage_urbain),
    path('ressourceZone/upload', upload_ressource_zone),
    # path('locality/upload', LocalityViewset.as_view()),
    # path('zone/upload', ZoneViewset.as_view()),
    # path('paysageUrbain/upload', PaysageUrbainViewset.as_view()),
    # path('ressourceZone/upload', RessourceZoneViewset.as_view()),
]