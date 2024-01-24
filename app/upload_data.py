#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arddelbeeVisualisation.settings')

# csv imports
import csv
from .models import *
from .serializer import *

# import the @api decorator
from rest_framework.decorators import api_view
# import the Response model
from rest_framework.response import Response


@api_view(['GET', 'POST'])
# read csv file and use Finance model to add in database
def upload_finance(request):
    data = './datas/Finance.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing Finance {row[0]}...")
            finance = Finance(
                enr = int(row[0]),
                ID_Finance = int(row[1]) if type(row[1]) != str else 0,
                IDZone = int(row[2]) if type(row[2]) != str else 0,
                IDExercice = int(row[3]) if type(row[3]) != str else 0,
                Budget = float(row[4]) if type(row[4]) != str else 0.0,
                BudgetPrevu = float(row[5]) if type(row[5]) != str else 0.0,
                FPrevu = float(row[6]) if type(row[6]) != str else 0.0,
                FRealise = float(row[7]) if type(row[7]) != str else 0.0,
                IPrevu = float(row[8]) if type(row[8]) != str else 0.0,
                IRealise = float(row[9]) if type(row[9]) != str else 0.0,
                DPrevu = float(row[10]) if type(row[10]) != str else 0.0,
                DRealise = float(row[11]) if type(row[11]) != str else 0.0,
                RPrevu = float(row[12]) if type(row[12]) != str else 0.0,
                RRealise = float(row[13]) if type(row[13]) != str else 0.0,
            )
            finance.save()
    return Response(FinanceSerializer(finance).data)


@api_view(['GET', 'POST'])
# read csv file and use Financement model to add in database
def upload_financement(request):
    data = './datas/Financement.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing Financement {row[0]}...")
            ressource_zone = Financement(
                Enr = int(row[0]),
                ID_Source = int(row[1]),
                ID_Finance = int(row[2]),
                IDTFinance = row[3],
                Provenance = row[4],
                DateDebut = row[5],
                DateFin = row[6],
                MontantPrevu = float(row[7]),
                MontantRealise = float(row[8]),
                Observation = row[9],
            )
            ressource_zone.save()
    return Response(FinancementSerializer(ressource_zone).data)


@api_view(['GET', 'POST'])
# read csv file and use Infrastructure model to add in database
def upload_infrastructure(request):
    data = './datas/Infrastructure.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing Infrastructure {row[0]}...")
            infrastructure = Infrastructure(
                Enr=row[0],
                ID_Infrastructure=row[1],
                IDZone=row[2],
                Libelle=row[3],
                Etat=row[4],
                CoordX=row[5],
                CoordY=row[6], 
                CoordZ=row[7],
                Qte = row[8],
                NWPT = row[9],
                Beneficiaire = row[10],
                Date = row[11],
                Observation = row[12],
                GroupeInfrastructure = row[13]
            )
            infrastructure.save()
    return Response(InfrastructureSerializer(infrastructure).data)


@api_view(['GET', 'POST'])
# read csv file and use Localite model to add in database
def upload_localite(request):
    data = './datas/Localite.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        print(csv_reader)
        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing Localite {row[0]}...")
            localite = Localite(
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
            localite.save()
    return Response(LocaliteSerializer(localite).data)


@api_view(['GET', 'POST'])
# read csv file and use MInfrastructure model to add in database
def upload_m_infrastructure(request):
    data = './datas/MInfrastructures.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing MInfrastructure {row[0]}...")
            minfrastructure = MInfrastructure(
                Enr = row[0],
                MInfrastructure = row[1],
                IDCadre = row[2],
                TInfrastructures = row[3],
                IDMInfrastructure = row[4],
                IDTInfrastructure = row[5],
            )
            minfrastructure.save()
    return Response(MInfrastructureSerializer(minfrastructure).data)

@api_view(['GET', 'POST'])
# read csv file and use Ministere model to add in database
def upload_ministere(request):
    data = './datas/Ministere.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing Ministere {row[0]}...")
            ministere = Ministere(
                Enr = row[0],
                IDSecteur = row[1],
                IDChapitre = row[2],
                CodeChapitre = row[3],
                Libelle = row[4],
                LibelleAng = row[5],
                Responsable = row[6],
                Ministere = row[7],
                Objectifs = row[8],
                Description = row[9],
                Strategie = row[10],
            )
            ministere.save()
    return Response(MinistereSerializer(ministere).data)

@api_view(['GET', 'POST'])
# read csv file and use ODDCible model to add in database
def upload_oddcible(request):
    data = './datas/ODDCibles_par_Ministere.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing ODDCible {row[0]}...")
            odd_cible = ODDCible(
                Enr = row[0],
                IDODDCibles = row[1],
                IDChapitre = row[2],
                IDCorrelation = row[3],
                ID = row[4],
            )
            odd_cible.save()
    return Response(ODDCibleSerializer(odd_cible).data)

@api_view(['GET', 'POST'])
# read csv file and use model to add in database
def upload_pays(request):
    data = './datas/Pays.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing Country {row[0]}...")
            country = Pays(
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

    return Response(PaysSerializer(country).data) # Response(country)

@api_view(['GET', 'POST'])
# read csv file and use PaysageUrbain model to add in database
def upload_paysage_urbain(request):
    data = './datas/PaysagesUrbains.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing Paysage Urbain {row[0]}...")
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
# read csv file and use PotentialiteDesZones model to add in database
def upload_potentialite_des_zones(request):
    data = './datas/PotentialitesDesZones.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing PotentialiteDesZones {row[0]}...")
            potentialite = PotentialitesDesZones(
                Enr = row[0],
                ID_Potentialite = row[1],
                IDZoneIDCadre = row[2],
                Potentialites = row[3],
                Ressources = row[4],
                IDZone = row[5],
                IDCadre = row[6],
            )
            potentialite.save()
    return Response(PotentialitesDesZonesSerializer(potentialite).data)

@api_view(['GET', 'POST'])
# read csv file and use Probleme model to add in database
def upload_probleme(request):
    data = './datas/Probleme.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing Probleme {row[0]}...")
            probleme = Probleme(
                Enr = row[0],
                IDZoneIDCadre = row[1],
                ID_Probleme = row[2],
                IDProbleme = row[3],
                Probleme = row[4],
                IDZone = row[5],
                Archive = row[6],
                IDCadre = row[7],
                IDSource = row[8],
                _MiseAJour = row[9],
            )
            probleme.save()
    return Response(ProblemeSerializer(probleme).data)


@api_view(['GET', 'POST'])
# read csv file and use ProgrammeDesMinisteres model to add in database
def upload_programme_des_ministeres(request):
    data = './datas/ProgrammesDesMinisteres.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing ProgrammeDesMinisteres {row[0]}...")
            probleme = ProgrammesDesMinisteres(
                Enr = row[0],
                IDChapitre = row[1],
                IDProgramme = row[2],
                CodeProgramme = row[3],
                Libelle = row[4],
                Objectifs = row[5],
                LibelleAng = row[6],
                Coordination = row[7],
                horizon = row[8],
                Date_debut = row[9],
                Date_fin = row[10],
                Montant = row[11],
                Responsable = row[12],
                Description = row[13],
                Axes = row[14],
                Strategie = row[15],
                Resultats = row[16],
                hypothese = row[17],
            )
            probleme.save()
    return Response(ProgrammesDesMinisteresSerializer(probleme).data)


@api_view(['GET', 'POST'])
# read csv file and use ProgrammeDesMinisteres model to add in database
def upload_provenance_des_finances(request):
    data = './datas/ProvenancesFinances.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing ProvenancesFinances {row[0]}...")
            provenance = ProvenanceFinance(
                Enr = row[0],
                ID_Source = row[1],
                ID_Finance = row[2],
                IDTFinance = row[3],
                Provenance = row[4],
                DateDebut = row[5],
                DateFin = row[6],
                MontantPrevu = row[7],
                MontantRealise = row[8],
                Observation = row[9],
            )
            provenance.save()
    return Response(ProvenanceFinanceSerializer(provenance).data)


@api_view(['GET', 'POST'])
# read csv file and use ProgrammeDesMinisteres model to add in database
def upload_region(request):
    data = './datas/Region.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing Region {row[0]}...")
            region = Region(
                Enr = row[0],
                Code_Region = row[1],
                Libelle = row[2],
                Masculin = row[3],
                Feminin = row[4],
                Total = row[5],
                Code_Pays = row[6],
                Accessible = row[7],
                DateCreation = row[8],
                Densite = row[9],
                Superficie = row[10],
                NbDepartement = row[11],
                NbCommune = row[12],
                NbLocalite = row[13],
            )
            region.save()
    return Response(RegionSerializer(region).data)


@api_view(['GET', 'POST'])
# read csv file and use ProgrammeDesMinisteres model to add in database
def upload_ressource(request):
    data = './datas/Ressources.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing Ressource {row[0]}...")
            ressource = Ressource(
                enr = row[0],
                Ressource = row[1],
                IDRessource = row[2],
                NomUsuel = row[3],
                NomScientifique = row[4],
                NomCommercial = row[5],
                IDTypesRessouces = row[6],
            )
            ressource.save()
    return Response(RessourceSerializer(ressource).data)


# @api_view(['GET', 'POST'])
# # read csv file and use RessourcesHumaines model to add in database
# def upload_ressource_humaines(request):
#     data = './datas/RessourcesHumaines.csv'
#     # read csv file
#     with open(data, 'r') as file:
#         csv_reader = csv.reader(file, delimiter=';')
#         next(csv_reader)  # skip header row

#         # use model to add data to the database
#         for row in csv_reader:
#             print(f"Importing RessourcesHumaines {row[0]}...")
#             ressource_humaine = RessourcesHumaines(
                
#             )
#             ressource_humaine.save()
#     return Response(RessourcesHumainesSerializer(ressource_humaine).data)



@api_view(['GET', 'POST'])
# read csv file and use RessourceZone model to add in database
def upload_ressource_zone(request):
    data = './datas/RessourcesZone.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing Ressource Zone {row[0]}...")
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

@api_view(['GET', 'POST'])
# read csv file and use Zone model to add in database
def upload_zone(request):
    data = './datas/Zone.csv'
    # read csv file
    with open(data, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip header row

        # use model to add data to the database
        for row in csv_reader:
            print(f"Importing Zone {row[0]}...")
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

