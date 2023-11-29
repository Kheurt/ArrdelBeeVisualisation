"""
User Model
"""
from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthUser(AbstractUser):
    
    def str(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

"""
Country
Locality
Zone
PaysageUrbain
RessourceZone
"""

from django.db import models

""" Class Country which specify the contry with the following fields 
    N° Enr.
    Code_Pays
    Libelle
    Masculin
    Feminin
    Total
    Accessible
    date_Creation
    Densité
    Superficie
    nbr_Region
    nbr_Departement
    nbr_Commune
    nbr_Localité
    date_Indépendance
    date_Reunification
    date_Unification
"""
class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    enr = models.IntegerField()
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=255) # Libelle
    male = models.IntegerField()
    female = models.IntegerField()
    total = models.IntegerField()
    # Total = models.CharField(max_length=255)
    accessible = models.CharField(max_length=255)
    date_creation = models.CharField(max_length=255)
    density = models.CharField(max_length=255)
    aera = models.CharField(max_length=255)
    nbr_Region = models.CharField(max_length=255)
    nbr_Departement = models.CharField(max_length=255)
    nbr_Commune = models.CharField(max_length=255)
    nbr_Localite = models.CharField(max_length=255)
    date_Independance = models.CharField(max_length=255)
    date_Reunification = models.CharField(max_length=255)
    date_Unification = models.CharField(max_length=255)


"""
Localities
N° Enr.
CodeS_Localité 
Code_Commune 
Code_Localité
Libelle
MASCULIN
FEMININ
TOTAL
Chefferie
PNombreMenage
PHomme
PFemme
PNombrePersHandicapé
PEnfants_5ans
PEnfants_15ans
PPopulations
IEEcoleMaternelle
IEEcolePrimaire
IEEColeSécondaire
IEEColeTechnique
IHForage
IHPuits
IHAdductionEau
IHAutres
IHAutresDétails
ICSCSI
ICSCMA
ICSHopital
ICSPrivée
ICSAutres
ICSAutresDétails
ISEPFoyers
ISEPCentreFemme
ISEPCentreMultifonctionnel 
ISEPCentreSociaux 
ISEPAutres
ISEPAutresDétails 
EPMMagasins
EPMMarchés
EPMAbbatoir
EPMGareRoutière
EPMParcàBetail
ACElectrification 
ACTéléphone
AVRouteBitumée
AVRouteEnTerreAménagé
AVPiste
ERAccessibleTouteSaison
ERInaccessibleEnSaisonDePluie
ERInaccessibleEnTouteSaison
ONombreQuartier
OExistenceComitéDeveloppement
Accessible

"""
class Locality(models.Model):

    id = models.BigAutoField(primary_key=True)
    enr = models.IntegerField()
    CodeS_Localite = models.IntegerField(null=True)
    Code_Commune = models.IntegerField()
    Code_Localite = models.IntegerField()
    Libelle = models.CharField(max_length=255)
    MASCULIN = models.IntegerField()
    FEMININ = models.IntegerField()
    TOTAL = models.IntegerField()
    Chefferie = models.IntegerField()
    PNombreMenage = models.IntegerField()
    PHomme = models.IntegerField()
    PFemme = models.IntegerField()
    PNombrePersHandicape = models.IntegerField()
    PEnfants_5ans = models.IntegerField()
    PEnfants_15ans = models.IntegerField()
    PPopulations = models.IntegerField()
    IEEcoleMaternelle = models.IntegerField()
    IEEcolePrimaire = models.IntegerField()
    IEEColeSecondaire = models.IntegerField()
    IEEColeTechnique = models.IntegerField()
    IHForage = models.IntegerField()
    IHPuits = models.IntegerField()
    IHAdductionEau = models.IntegerField()
    IHAutres = models.IntegerField()
    IHAutresDetails = models.IntegerField()
    ICSCSI = models.IntegerField()
    ICSCMA = models.IntegerField()
    ICSHopital = models.IntegerField()
    ICSPrivee = models.IntegerField()
    ICSAutres = models.IntegerField()
    ICSAutresDetails = models.IntegerField()
    ISEPFoyers = models.IntegerField()
    ISEPCentreFemme = models.IntegerField()
    ISEPCentreMultifonctionnel = models.IntegerField()
    ISEPCentreSociaux = models.IntegerField()
    ISEPAutres = models.IntegerField()
    ISEPAutresDetails = models.IntegerField()
    EPMMagasins = models.IntegerField()
    EPMMarches = models.IntegerField()
    EPMAbbatoir = models.IntegerField()
    EPMGareRoutiere = models.IntegerField()
    EPMParcaBetail = models.IntegerField()
    ACElectrification = models.IntegerField()
    ACTelephone = models.IntegerField()
    AVRouteBitumee = models.IntegerField()
    AVRouteEnTerreAmenage = models.IntegerField()
    AVPiste = models.IntegerField()
    ERAccessibleTouteSaison = models.IntegerField()
    ERInaccessibleEnSaisonDePluie = models.IntegerField()
    ERInaccessibleEnTouteSaison = models.IntegerField()
    ONombreQuartier = models.IntegerField()
    OExistenceComiteDeveloppement = models.IntegerField()
    Accessible = models.IntegerField()


"""
Zones
N° Enr.
IDZone
Code_Pays
Pays
Code_Region
Région
Code_Departement
Departement
Code_Commune
Commune
Code_Localité
Localité
Zone
ZNiveau
NbRegion
NbDepartement
NbCommune
NbLocalité
Superficie
Densité
Adresse
Date
EMail
Telephone
Icone
Image
Masculin
Feminin
Total
Accessible
DelimitationJSON
Limites
Localisation
"""
class Zone(models.Model):

    id = models.BigAutoField(primary_key=True)
    enr = models.IntegerField()
    IDZone = models.CharField(max_length=255)
    CodePays = models.CharField(max_length=255)
    Pays = models.CharField(max_length=255)
    CodeRegion = models.CharField(max_length=255)
    Region = models.CharField(max_length=255)
    CodeDepartement = models.CharField(max_length=255)
    Departement = models.CharField(max_length=255)
    CodeCommune = models.CharField(max_length=255)
    Commune = models.CharField(max_length=255)
    CodeLocalite = models.CharField(max_length=255)
    Localite = models.CharField(max_length=255)
    Zone = models.CharField(max_length=255)
    ZNiveau = models.CharField(max_length=255)
    NbRegion = models.CharField(max_length=255)
    NbDepartement = models.CharField(max_length=255)
    NbCommune = models.CharField(max_length=255)
    NbLocalite = models.CharField(max_length=255)
    Superficie = models.CharField(max_length=255)
    Densite = models.CharField(max_length=255)
    Adresse = models.CharField(max_length=255)
    Date = models.CharField(max_length=255)
    EMail = models.CharField(max_length=255)
    Telephone = models.CharField(max_length=255)
    Icone = models.CharField(max_length=255)
    Image = models.CharField(max_length=255)
    Masculin = models.CharField(max_length=255)
    Feminin = models.CharField(max_length=255)
    Total = models.CharField(max_length=255)
    Accessible = models.CharField(max_length=255)
    DelimitationJSON = models.CharField(max_length=255)
    Limites = models.CharField(max_length=255)
    Localisation = models.CharField(max_length=255)


"""
Paysage Urbain
N° Enr.
UnitePaysage
ID_PUGE
IDZone
Utilisation
Potentialité
Utilisateur
Probleme
Causes
Consequences
Solutions
"""
class PaysageUrbain(models.Model):

    id = models.BigAutoField(primary_key=True)
    enr = models.IntegerField()
    UnitePaysage = models.CharField(max_length=255)
    ID_PUGE = models.CharField(max_length=255)
    IDZone = models.CharField(max_length=255)
    Utilisation = models.TextField()#.CharField(max_length=255) #
    Potentialite = models.TextField()#.CharField(max_length=255) #
    Utilisateur = models.TextField()#.CharField(max_length=255) #
    Probleme = models.TextField()#.CharField(max_length=255) #
    Causes = models.TextField()
    Consequences = models.TextField()
    Solutions = models.TextField()

"""
Ressource Zone
N° Enr.
IDPRessources
IDZone
Ressource
Caractèristique
UtilisationActuelle
Potentialité
Contrainte
ActionaMener
AccèsControle
Archivé
IDSource;_MiseAJour
CoordX
CoordY
CoordZ
ModeGestion
Tendances
"""
class RessourceZone(models.Model):
    id = models.BigAutoField(primary_key=True)
    enr = models.IntegerField()
    IDPRessources = models.CharField(max_length=255)
    IDZone = models.CharField(max_length=255)
    Ressource = models.CharField(max_length=255)
    Caracteristique = models.TextField()
    UtilisationActuelle = models.TextField()
    Potentialite = models.TextField()
    Contrainte = models.TextField()
    ActionaMener = models.TextField()
    AccesControle = models.TextField()
    Archive = models.TextField()
    IDSource = models.CharField(max_length=255)
    MiseAJour = models.CharField(max_length=255)
    CoordX = models.CharField(max_length=255)
    CoordY = models.CharField(max_length=255)
    CoordZ = models.CharField(max_length=255)
    ModeGestion = models.CharField(max_length=255)
    Tendances = models.CharField(max_length=255)

