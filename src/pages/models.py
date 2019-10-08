from django.db import models

# Create your models here.

class categories(models.Model):
    UserID = models.IntengerField(max_length=50, blank=True, primary_key=True)
    UserName = models.CharField(max_length=50, blank=True)
    UserEmail = models.CharField(max_length=50, blank=True)
    UserPassword = models.CharField(max_length=50, blank=True)
    SpecialistServices = models.IntengerField(max_length=50, blank=True)
    PreventativeCare = models.IntengerField(max_length=50, blank=True)
    DiagnosticTest = models.IntengerField(max_length=50, blank=True)
    GenericDrugs = models.IntengerField(max_length=50, blank=True)
    OutpatientSurgery = models.IntengerField(max_length=50, blank=True)
    ImmediateMedicalAttention = models.IntengerField(max_length=50, blank=True)
    HospitalStay = models.IntengerField(max_length=50, blank=True)
    OutpatientInpatient = models.IntengerField(max_length=50, blank=True)
    Pregnancy = models.IntengerField(max_length=50, blank=True)
    HomeHealthCare = models.IntengerField(mmax_length=50, blank=True)
    RehabilationServices = models.IntengerField(max_length=50, blank=True)
    SkilledNursingCare = models.IntengerField(max_length=50, blank=True)
