from django.contrib import admin
from .models import *

""" Register all models in django admin. """
# Register all models in django admin
admin.site.register(Country)
admin.site.register(Locality)
admin.site.register(Zone)
admin.site.register(PaysageUrbain)
admin.site.register(RessourceZone)
