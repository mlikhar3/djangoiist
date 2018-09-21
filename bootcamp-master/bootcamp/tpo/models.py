from django.contrib.auth.models import *
from django.db import models
from django import forms

FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)

CHOICES = (
        ("1", "ONE"),
        ("2", "TWO"),
)

class LeavePage(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Subject = models.CharField(max_length=20)
    Message = models.TextField()

    def __str__(self):
        return self.Name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
   
   

class Sector(models.Model):
    SECTOR = (("Core_Engineering", "Core_Engineering"), ("Consulting", "Consulting"), ("IT", "IT"), ("Finanace", "Finanace"))


class Choices(models.Model):
    description = models.CharField(max_length=300)


class Profile(models.Model):
   user = models.ForeignKey(User,related_name='+', blank=True)
   the_choices = models.OneToOneField(Choices)


class CompanyProfile(models.Model):
    #TYPE = (("government","government"),("Private","Private"),("Semi-Governamet", "Semi-Governamet"),("Public", "Public"))
    GD = (("YES","YES"),("NO","NO"))
    Name_Of_the_Company = models.CharField(max_length=100,blank=True,null=True)
    Address = models.TextField()
    Type = models.CharField(max_length=20,blank=True,null=True)
    Indstry_sctr_Core = models.CharField(max_length=10,blank=True,null=True)
    Indstry_sctr_consulting = models.CharField(max_length=10,blank=True,null=True)
    Indstry_sctr_IT = models.CharField(max_length=10,blank=True,null=True)
    Indstry_sctr_Finanace = models.CharField(max_length=10,blank=True,null=True)
    Indstry_sctr_Govrnt = models.CharField(max_length=10,blank=True,null=True)
    Indstry_sctr_Other = models.CharField(max_length=100,blank=True,null=True)
    req_functional_areas_Red = models.CharField(max_length=10,blank=True,null=True)
    req_functional_areas_Maintenance = models.CharField(max_length=10,blank=True,null=True)
    req_functional_areas_Design = models.CharField(max_length=10,blank=True,null=True)
    req_functional_areas_Production = models.CharField(max_length=10,blank=True,null=True)
    req_functional_areas_RD = models.CharField(max_length=10,blank=True,null=True)
    req_functional_areas_Others = models.CharField(max_length=200,blank=True,null=True)
    req_functional_areas_Finance = models.CharField(max_length=10,blank=True,null=True)
    VsnandInterest = models.CharField(max_length=10,blank=True,null=True)
    PrsnName = models.CharField(max_length=200,blank=True,null=True)
    PrsnDesignation = models.CharField(max_length=200,blank=True,null=True)
    PrsnPhone = models.CharField(max_length=200,blank=True,null=True)
    PrsnEmail = models.CharField(max_length=200,blank=True,null=True)
    CGPA = models.CharField(max_length=10,blank=True,null=True)
    XII_perc = models.CharField(max_length=10,blank=True,null=True)
    X_perc = models.CharField(max_length=200,blank=True,null=True)
    SpecialisationPG = models.CharField(max_length=200,blank=True,null=True)
    Age_limits = models.CharField(max_length=200,blank=True,null=True)
    Test_Written = models.CharField(max_length=10,blank=True,null=True)
    Test_Aptitude = models.CharField(max_length=10,blank=True,null=True)
    Test_Online = models.CharField(max_length=10,blank=True,null=True)
    Test_Technical = models.CharField(max_length=10,blank=True,null=True)
    Test_Others = models.CharField(max_length=10,blank=True,null=True)
    GD = models.CharField(max_length=20,blank=True,null=True)
    PITechnical = models.CharField(max_length=10,blank=True,null=True)
    PIHR = models.CharField(max_length=10,blank=True,null=True)
    PIOthers = models.CharField(max_length=100,blank=True,null=True)
    ServiceAgreement = models.CharField(max_length=100,blank=True,null=True)
    TrainingPeriod = models.CharField(max_length=100,blank=True,null=True)
    
    AllStreamsBE = models.CharField(max_length=10,blank=True,null=True)
    AllStreamsMCA = models.CharField(max_length=10,blank=True,null=True)
    AllStreamsMBA = models.CharField(max_length=10,blank=True,null=True)
    AllStreamsPHARMA = models.CharField(max_length=10,blank=True,null=True)
    
    #IIST
    ChemBE = models.CharField(max_length=10,blank=True,null=True)
    CivilBE = models.CharField(max_length=10,blank=True,null=True)
    ComputerBE = models.CharField(max_length=10,blank=True,null=True)
    MechBE = models.CharField(max_length=10,blank=True,null=True)
    ECBE = models.CharField(max_length=10,blank=True,null=True)
    ELECTRICALBE = models.CharField(max_length=10,blank=True,null=True)

    #IICA
    MCA = models.CharField(max_length=10,blank=True,null=True)
    
    #IIMR
    BBA=models.CharField(max_length=10,blank=True,null=True)
    MBA = models.CharField(max_length=10,blank=True,null=True)
    #IIP
    PharmaBACH = models.CharField(max_length=10,blank=True,null=True)
    PharmaMAST = models.CharField(max_length=10,blank=True,null=True)
    
    In_Hand = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.Name_Of_the_Company


class Feedback(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Subject = models.CharField(max_length=20)
    Message = models.TextField()

    def __str__(self):
        return self.Name




