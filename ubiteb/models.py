from django.db import models
from django.utils import timezone
from django.utils import timezone
from django.urls import reverse
import datetime
from django_countries.fields import CountryField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _

# Create your models here.

class Alumni(models.Model):
    
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    
    #STATUS_CHOICES = [("graduated", "Graduated"), ("not graduated", "Not Graduated")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]
    
    PROGRAM_LEVEL_CHOICES =[("certificate", "Certificate"), ("diploma", "Diploma")]
    
    PROGRAM_CHOICES = [('ndict', 'NDICT'), ('ndbce', 'NDBCE')]
    
    TRANSCRIPT_CHOICES = [("received", "Received"), ("not received", "Not Received")]
    
    CERTIFICATE_CHOICES = [("received", "Received"), ("not received", "Not Received")]
    
    CENTER_CHOICES = [('mbi', 'MBI'), ('mubs', 'MUBS')]
    
    EMPLOYMENT_STATUS_CHOICES = [("employed", "Employed"), ("unemployed", "Unemployed")]
    
    EMPLOYEMENT_ENTITY_CHOICES = [("government", "Government"), ("private", "Private"),("ngo", "NGO"), ("missionnary", "Missionary"), ("none", "None")]
    


    #current_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    surname = models.CharField(max_length=200, default=None)
    othernames = models.CharField(max_length=200, default=None)
    regNo = models.CharField(max_length=200, unique=True)
    dob = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    phone_number = PhoneNumberField()
    email=models.EmailField(max_length=50, unique=True)
    nationality = CountryField()
    district = models.CharField(max_length=30, blank=True)
    program_level = models.CharField(max_length=30, choices=PROGRAM_LEVEL_CHOICES, default='certificate')
    program = models.CharField(max_length=50, choices=PROGRAM_CHOICES, default='ndict')
    center = models.CharField(max_length=50, choices= CENTER_CHOICES, default='mbi')
    start_year = models.IntegerField(_('Start Year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    completion_year = models.IntegerField(_('Completion Year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    transcript_status = models.CharField(max_length=30, choices=TRANSCRIPT_CHOICES, default='received')
    certificate_status = models.CharField(max_length=30, choices=CERTIFICATE_CHOICES, default='received')
    employment_status = models.CharField(max_length=40, choices=EMPLOYMENT_STATUS_CHOICES, default='employed')
    employment_entity = models.CharField(max_length=40, choices=EMPLOYEMENT_ENTITY_CHOICES, default='government')
    
        
    def serialize_nationality(self):
        return str(self.nationality)
    
    

    class Meta:
        ordering = ["surname", "othernames", "regNo"]

    def __str__(self):
        return f"{self.surname} {self.othernames} {self.regNo} ({self.program_level}, {self.program})"

    def get_absolute_url(self):
        return reverse("alumnus-detail", kwargs={"pk": self.pk})


    
    
