from django.urls import path, include
from .views import *
from .upload_data import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register('pays', PaysViewset),
router.register('localite', LocaliteViewset),
router.register('zone', ZoneViewset),
router.register('paysageUrbain', PaysageUrbainViewset),
router.register('ressourceZone', RessourceZoneViewset),

# Pays
# Localite
# Zone
# PaysageUrbain
# RessourceZone

urlpatterns = [
    path('', include(router.urls)), 
    path('upload/finance', upload_finance),
    path('upload/financement', upload_financement),
    path('upload/infrastructure', upload_infrastructure),
    path('upload/localite', upload_localite),
    path('upload/minfrastructure', upload_m_infrastructure),
    path('upload/ministere', upload_ministere),
    path('upload/oddcible', upload_oddcible),
    path('upload/pays', upload_pays),
    path('upload/paysageUrbain', upload_paysage_urbain),
    path('upload/potentialitesDesZones', upload_potentialite_des_zones),
    path('upload/probleme', upload_probleme),
    path('upload/programmesDesMinisteres', upload_programme_des_ministeres),
    path('upload/provenancesFinances', upload_provenance_des_finances),
    path('upload/region', upload_region),
    path('upload/ressources', upload_ressource),
    # path('upload/ressourceHumaine', upload_ressource_humaine),
    path('upload/ressourceZone', upload_ressource_zone),
    path('upload/zone', upload_zone),

    # path('localite/upload', LocaliteViewset.as_view()),
    # path('zone/upload', ZoneViewset.as_view()),
    # path('paysageUrbain/upload', PaysageUrbainViewset.as_view()),
    # path('ressourceZone/upload', RessourceZoneViewset.as_view()),
]