#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arddelbeeVisualisation.settings')

# csv imports
import csv
from .models import Country, Locality, Zone, PaysageUrbain, RessourceZone
from .serializer import CountrySerializer, LocalitySerializer, ZoneSerializer, PaysageUrbainSerializer, RessourceZoneSerializer

# import the @api decorator
from rest_framework.decorators import api_view
# import the Response model
from rest_framework.response import Response



@api_view(['GET', 'POST'])
# read csv file and use model to add in database
def upload_country(request):
    data = '../datas/Pays.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(row)
            country = Country(
                enr=row[0],
                code=row[1],
                name=row[2], # Libelle
                male=int(row[3]),
                female=int(row[4]),
                total=int(row[5]),
                # Total=row[6],
                accessible=row[6],
                date_creation=row[7],
                density=row[8],
                aera=row[9],
                nbr_Region=row[10],
                nbr_Departement=row[11],
                nbr_Commune=row[12],
                nbr_Localite=row[13],
                date_Independance=row[14],
                date_Reunification=row[15],
                date_Unification=row[16]
            )
            country.save()

    return Response(CountrySerializer(country).data) # Response(country)

@api_view(['GET', 'POST'])
# read csv file and use Locality model to add in database
def upload_locality(request):
    data = '../datas/Localite.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        print(csv_reader)
        # use model to add data to the database
        for row in csv_reader:
            # print(row)
            locality = Locality(
                enr = int(row[0]),
                CodeS_Localite = int(row[1]) if type(row[1]) != str else 0,
                Code_Commune = int(row[2]) if type(row[2]) != str else 0,
                Code_Localite = int(row[3]) if type(row[3]) != str else 0,
                Libelle = row[4],
                MASCULIN = int(row[5]) if type(row[5]) != str else 0,
                FEMININ = int(row[6]) if type(row[6]) != str else 0,
                TOTAL = int(row[7]) if type(row[7]) != str else 0,
                Chefferie = int(row[8]) if type(row[8]) != str else 0,
                PNombreMenage = int(row[9]) if type(row[9]) != str else 0,
                PHomme = int(row[10]) if type(row[10]) != str else 0,
                PFemme = int(row[11]) if type(row[11]) != str else 0,
                PNombrePersHandicape = int(row[12]) if type(row[12]) != str else 0,
                PEnfants_5ans = int(row[13]) if type(row[13]) != str else 0,
                PEnfants_15ans = int(row[14]) if type(row[14]) != str else 0,
                PPopulations = int(row[15]) if type(row[15]) != str else 0,
                IEEcoleMaternelle = int(row[16]) if type(row[16]) != str else 0,
                IEEcolePrimaire = int(row[17]) if type(row[17]) != str else 0,
                IEEColeSecondaire = int(row[18]) if type(row[18]) != str else 0,
                IEEColeTechnique = int(row[19]) if type(row[19]) != str else 0,
                IHForage = int(row[20]) if type(row[20]) != str else 0,
                IHPuits = int(row[21]) if type(row[21]) != str else 0,
                IHAdductionEau = int(row[22]) if type(row[22]) != str else 0,
                IHAutres = int(row[23]) if type(row[23]) != str else 0,
                IHAutresDetails = int(row[24]) if type(row[24]) != str else 0,
                ICSCSI = int(row[25]) if type(row[25]) != str else 0,
                ICSCMA = int(row[26]) if type(row[26]) != str else 0,
                ICSHopital = int(row[27]) if type(row[27]) != str else 0,
                ICSPrivee = int(row[28]) if type(row[28]) != str else 0,
                ICSAutres = int(row[29]) if type(row[29]) != str else 0,
                ICSAutresDetails = int(row[30]) if type(row[30]) != str else 0,
                ISEPFoyers = int(row[31]) if type(row[31]) != str else 0,
                ISEPCentreFemme = int(row[32]) if type(row[32]) != str else 0,
                ISEPCentreMultifonctionnel = int(row[33]) if type(row[33]) != str else 0,
                ISEPCentreSociaux = int(row[34]) if type(row[34]) != str else 0,
                ISEPAutres = int(row[35]) if type(row[35]) != str else 0,
                ISEPAutresDetails = int(row[36]) if type(row[36]) != str else 0,
                EPMMagasins = int(row[37]) if type(row[37]) != str else 0,
                EPMMarches = int(row[38]) if type(row[38]) != str else 0,
                EPMAbbatoir = int(row[39]) if type(row[39]) != str else 0,
                EPMGareRoutiere = int(row[40]) if type(row[40]) != str else 0,
                EPMParcaBetail = int(row[41]) if type(row[41]) != str else 0,
                ACElectrification = int(row[42]) if type(row[42]) != str else 0,
                ACTelephone = int(row[43]) if type(row[43]) != str else 0,
                AVRouteBitumee = int(row[44]) if type(row[44]) != str else 0,
                AVRouteEnTerreAmenage = int(row[45]) if type(row[45]) != str else 0,
                AVPiste = int(row[46]) if type(row[46]) != str else 0,
                ERAccessibleTouteSaison = int(row[47]) if type(row[47]) != str else 0,
                ERInaccessibleEnSaisonDePluie = int(row[48]) if type(row[48]) != str else 0,
                ERInaccessibleEnTouteSaison = int(row[49]) if type(row[49]) != str else 0,
                ONombreQuartier = int(row[50]) if type(row[50]) != str else 0,
                OExistenceComiteDeveloppement = int(row[51]) if type(row[51]) != str else 0,
                Accessible = int(row[52]) if type(row[52]) != str else 0,
            )
            locality.save()
    return Response(LocalitySerializer(locality).data)

@api_view(['GET', 'POST'])
# read csv file and use Zone model to add in database
def upload_zone(request):
    data = '../datas/Zone.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            zone = Zone(
                enr=int(row[0]) if type(row[0]) != str else row[0],
                IDZone=row[1],
                CodePays=row[2],
                Pays=row[3],
                CodeRegion=row[4],
                Region=row[5],
                CodeDepartement=row[6],
                Departement=row[7],
                CodeCommune=row[8],
                Commune=row[9],
                CodeLocalite=row[10],
                Localite=row[11],
                Zone=row[12],
                ZNiveau=row[13],
                NbRegion=row[14],
                NbDepartement=row[15],
                NbCommune=row[16],
                NbLocalite=row[17],
                Superficie=row[18],
                Densite=row[19],
                Adresse=row[20],
                Date=row[21],
                EMail=row[22],
                Telephone=row[23],
                Icone=row[24],
                Image=row[25],
                Masculin=row[26],
                Feminin=row[27],
                Total=row[28],
                Accessible=row[29],
                DelimitationJSON=row[30],
                Limites=row[31],
                Localisation=row[32],
            )
            zone.save()
    return Response(ZoneSerializer(zone).data)

@api_view(['GET', 'POST'])
# read csv file and use PaysageUrbain model to add in database
def upload_paysage_urbain(request):
    data = '../datas/PaysagesUrbains.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            paysage_urbain = PaysageUrbain(
                enr=row[0],
                UnitePaysage=row[1],
                ID_PUGE=row[2],
                IDZone=row[3],
                Utilisation=row[4],
                Potentialite=row[5],
                Utilisateur=row[6],
                Probleme=row[7],
                Causes=row[8],
                Consequences=row[9],
                Solutions=row[10]
            )
            paysage_urbain.save()
    return Response(PaysageUrbainSerializer(paysage_urbain).data)

@api_view(['GET', 'POST'])
# read csv file and use RessourceZone model to add in database
def upload_ressource_zone(request):
    data = '../datas/RessourcesZone.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(row)
            ressource_zone = RessourceZone(
                enr=row[0],
                IDPRessources=row[1],
                IDZone=row[2],
                Ressource=row[3],
                Caracteristique=row[4],
                UtilisationActuelle=row[5],
                Potentialite=row[6],
                Contrainte=row[7],
                ActionaMener=row[8],
                AccesControle=row[9],
                Archive=row[10],
                IDSource=row[11],
                MiseAJour=row[12],
                CoordX=row[13],
                CoordY=row[14],
                CoordZ=row[15],
                ModeGestion=row[16],
                Tendances=row[17]
            )
            ressource_zone.save()
    return Response(RessourceZoneSerializer(ressource_zone).data)

