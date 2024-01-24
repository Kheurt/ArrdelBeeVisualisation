"""
User Model
"""
from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthUser(AbstractUser):
    
    def str(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

"""
Pays
Localite
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
class Pays(models.Model):
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

    def __str__(self) -> str:
        return f"N° Enr. {self.enr} - {self.name}"


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
class Localite(models.Model):

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

    def __str__(self) -> str:
        return f"N° Enr. {self.enr} - {self.Libelle}"


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

    def __str__(self) -> str:
        return f"N° Enr. {self.enr} - {self.IDZone} : {self.Zone}, {self.Pays} ({self.CodePays}), {self.Region} ({self.CodeRegion}), {self.Departement} ({self.CodeDepartement}), {self.Commune} ({self.CodeCommune}), {self.Localite} ({self.CodeLocalite})"


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

    def __str__(self) -> str:
        return f"N° Enr. {self.enr} - {self.UnitePaysage}"

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

    def __str__(self) -> str:
        return f"N° Enr. {self.enr} - {self.Ressource}. Map: ({self.CoordX}, {self.CoordY}, {self.CoordZ})"

"""
N° Enr.
Ressource
IDRessource
NomUsuel
NomScientifique
NomCommercial
IDTypesRessouces
"""
class Ressource(models.Model):

    id = models.BigAutoField(primary_key=True)
    enr = models.IntegerField()
    Ressource = models.CharField(max_length=255)
    IDRessource = models.CharField(max_length=255)
    NomUsuel = models.CharField(max_length=255)
    NomScientifique = models.CharField(max_length=255)
    NomCommercial = models.CharField(max_length=255)
    IDTypesRessouces = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Ressource N°{self.enr}"


"""
N° Enr.
ID_Finance
IDZone
IDExercice
Budget
BudgetPrevu
FPrevu
FRealise
IPrevu
IRealise
DPrevu
DRealise
RPrevu
RRealise
"""
class Finance(models.Model):

    id = models.BigAutoField(primary_key=True)
    enr = models.IntegerField()
    ID_Finance = models.BigIntegerField()
    IDZone = models.BigIntegerField()
    IDExercice = models.IntegerField() #Année de l'excercice
    Budget = models.FloatField()
    BudgetPrevu = models.FloatField()
    FPrevu = models.FloatField()
    FRealise = models.FloatField()
    IPrevu = models.FloatField()
    IRealise = models.FloatField()
    DPrevu = models.FloatField()
    DRealise = models.FloatField()
    RPrevu = models.FloatField()
    RRealise = models.FloatField()

    def __str__(self) -> str:
        return f"Finance N°{self.enr}"

"""
N° Enr.
ID_Source
ID_Finance
IDTFinance
Provenance
DateDebut
DateFin
MontantPrevu
MontantRealise
Observation
"""

class Financement(models.Model):
    id = models.BigAutoField(primary_key=True)
    Enr = models.IntegerField()
    ID_Source = models.BigIntegerField()
    ID_Finance = models.BigIntegerField()
    IDTFinance = models.CharField(max_length=255)
    Provenance = models.CharField(max_length=255)
    DateDebut = models.CharField(max_length=255)
    DateFin = models.CharField(max_length=255)
    MontantPrevu = models.FloatField()
    MontantRealise = models.FloatField()
    Observation = models.TextField()

    def __str__(self) -> str:
        return f"Financement N°{self.Enr}"

"""
N° Enr.
ID_Infrastructure
IDZone
Libelle
Etat
CoordX
CoordY
CoordZ
Qte
NWPT
Beneficiaire
Date
Observation
GroupeInfrastructure
"""
class Infrastructure (models.Model):
    Enr = models.IntegerField()
    ID_Infrastructure = models.CharField(max_length=255)
    IDZone = models.CharField(max_length=255)
    Libelle = models.CharField(max_length=255)
    Etat = models.CharField(max_length=255)
    CoordX = models.CharField(max_length=255)
    CoordY = models.CharField(max_length=255)
    CoordZ = models.CharField(max_length=255)
    Qte = models.CharField(max_length=255)
    NWPT = models.CharField(max_length=255)
    Beneficiaire = models.CharField(max_length=255)
    Date = models.CharField(max_length=255)
    Observation = models.TextField()
    GroupeInfrastructure = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Infrastructure N°{self.Enr}: {self.Libelle}"


"""
N° Enr.
MInfrastructure
IDCadre
TInfrastructures
IDMInfrastructure
IDTInfrastructure
"""
class MInfrastructure(models.Model):
    Enr = models.IntegerField()
    MInfrastructure = models.CharField(max_length=255)
    IDCadre = models.CharField(max_length=255)
    TInfrastructures = models.CharField(max_length=255)
    IDMInfrastructure = models.CharField(max_length=255)
    IDTInfrastructure = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Infrastructure Ministerielle N°{self.Enr}: {self.MInfrastructure}"

"""
N° Enr.
IDSecteur
IDChapitre
CodeChapitre
Libelle
LibelleAng
Responsable
Ministere
Objectifs
Description
Strategie
"""
class Ministere(models.Model):
    Enr = models.IntegerField()
    IDSecteur = models.CharField(max_length=255)
    IDChapitre = models.CharField(max_length=255)
    CodeChapitre = models.CharField(max_length=255)
    Libelle = models.CharField(max_length=255)
    LibelleAng = models.CharField(max_length=255)
    Responsable = models.CharField(max_length=255)
    Ministere = models.CharField(max_length=255)
    Objectifs = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Strategie = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Ministère N°{self.Enr}: {self.Libelle}"

"""
N° Enr.
IDODDCibles
IDChapitre
IDCorrelation
ID
"""
class ODDCible(models.Model):
    Enr = models.IntegerField()
    IDODDCibles = models.CharField(max_length=255)
    IDChapitre = models.CharField(max_length=255)
    IDCorrelation = models.CharField(max_length=255)
    ID = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"ODD N°{self.Enr} : {self.IDODDCibles}"

"""
N° Enr.
ID_Potentialite
IDZoneIDCadre
Potentialites
Ressources
IDZone
IDCadre
"""
class PotentialitesDesZones(models.Model):
    Enr = models.IntegerField()
    ID_Potentialite = models.CharField(max_length=255)
    IDZoneIDCadre = models.CharField(max_length=255)
    Potentialites = models.TextField()
    Ressources = models.TextField()
    IDZone = models.CharField(max_length=255)
    IDCadre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Potentialité N°{self.Enr}"

"""
N° Enr.
IDZoneIDCadre
ID_Probleme
IDProbleme
Probleme
IDZone
Archive
IDCadre
IDSource
_MiseAJour
"""
class Probleme(models.Model):
    Enr = models.IntegerField()
    IDZoneIDCadre = models.CharField(max_length=255)
    ID_Probleme = models.CharField(max_length=255)
    IDProbleme = models.CharField(max_length=255)
    Probleme = models.TextField()
    IDZone = models.CharField(max_length=255)
    Archive = models.CharField(max_length=255)
    IDCadre = models.CharField(max_length=255)
    IDSource = models.CharField(max_length=255)
    _MiseAJour = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Problème N°{self.Enr}"

"""
N° Enr.
IDChapitre
IDProgramme
CodeProgramme
Libelle
Objectifs
LibelleAng
Coordination
horizon
Date_debut
Date_fin
Montant
Responsable
Description
Axes
Strategie
Resultats
hypothese
"""
class ProgrammesDesMinisteres(models.Model):
    Enr = models.IntegerField()
    IDChapitre = models.CharField(max_length=255)
    IDProgramme = models.CharField(max_length=255)
    CodeProgramme = models.CharField(max_length=255)
    Libelle = models.CharField(max_length=255)
    Objectifs = models.CharField(max_length=255)
    LibelleAng = models.CharField(max_length=255)
    Coordination = models.CharField(max_length=255)
    horizon = models.CharField(max_length=255)
    Date_debut = models.CharField(max_length=255)
    Date_fin = models.CharField(max_length=255)
    Montant = models.CharField(max_length=255)
    Responsable = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Axes = models.CharField(max_length=255)
    Strategie = models.CharField(max_length=255)
    Resultats = models.CharField(max_length=255)
    hypothese = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Programme N°{self.Enr}"

"""
N° Enr.
ID_Source
ID_Finance
IDTFinance
Provenance
DateDebut
DateFin
MontantPrevu
MontantRealise
Observation
"""
class ProvenanceFinance(models.Model):
    Enr = models.IntegerField()
    ID_Source = models.CharField(max_length=255)
    ID_Finance = models.CharField(max_length=255)
    IDTFinance = models.CharField(max_length=255)
    Provenance = models.CharField(max_length=255)
    DateDebut = models.CharField(max_length=255)
    DateFin = models.CharField(max_length=255)
    MontantPrevu = models.CharField(max_length=255)
    MontantRealise = models.CharField(max_length=255)
    Observation = models.TextField()

    def __str__(self) -> str:
        return f"N°{self.Enr} : {self.ID_Source}"

"""
N° Enr.
Code_Region
Libelle
Masculin
Feminin
Total
Code_Pays
Accessible
DateCreation
Densite
Superficie
NbDepartement
NbCommune
NbLocalite
"""
class Region(models.Model):
    Enr = models.IntegerField()
    Code_Region = models.CharField(max_length=255)
    Libelle = models.CharField(max_length=255)
    Masculin = models.CharField(max_length=255)
    Feminin = models.CharField(max_length=255)
    Total = models.CharField(max_length=255)
    Code_Pays = models.CharField(max_length=255)
    Accessible = models.CharField(max_length=255)
    DateCreation = models.CharField(max_length=255)
    Densite = models.CharField(max_length=255)
    Superficie = models.CharField(max_length=255)
    NbDepartement = models.CharField(max_length=255)
    NbCommune = models.CharField(max_length=255)
    NbLocalite = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Région N°{self.Enr}: {self.Libelle}"

