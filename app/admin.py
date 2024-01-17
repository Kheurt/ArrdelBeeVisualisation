from django.contrib import admin
from .models import *

""" Register all models in django admin. """
# Register all models in django admin
admin.site.register(Pays)
admin.site.register(Localite)
admin.site.register(Zone)
admin.site.register(PaysageUrbain)
admin.site.register(RessourceZone)
admin.site.register(Ressource)
admin.site.register(Finance)
admin.site.register(Financement)
admin.site.register(Infrastructure)
admin.site.register(MInfrastructure)
admin.site.register(ODDCible)
admin.site.register(PotentialitesDesZones)
admin.site.register(Probleme)
admin.site.register(ProgrammesDesMinisteres)
admin.site.register(ProvenanceFinance)
admin.site.register(Region)
