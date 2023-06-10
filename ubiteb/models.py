from django.db import models
from django.utils import timezone
from django.utils import timezone
from django.urls import reverse
import datetime
from django_countries.fields import CountryField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _

from ubiteb.utils import get_centers_from_csv
from ubiteb.utils import get_districts_from_csv
from ubiteb.utils import get_programs_from_csv
from .utils import *


# Create your models here.

class Alumni(models.Model):
    
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    

    GENDER_CHOICES = [("Male", "Male"), ("Female", "Female")]
    
    PROGRAM_LEVEL_CHOICES =[("Higher Diploma", "Higher Diploma"),
                            ("Diploma", "Diploma"),
                            ("National Certificate", "National Certificate"),
                            ("Uganda Community of Polytechnic Certificate", "UCPC"),]
    
    TRANSCRIPT_CHOICES = [("Received", "Received"), ("Not Received", "Not Received")]
    
    CERTIFICATE_CHOICES = [("Received", "Received"), ("Not Received", "Not Received")]
    
    EMPLOYMENT_STATUS_CHOICES = [("Employed", "Employed"), ("Unemployed", "Unemployed")]
    
    EMPLOYEMENT_ENTITY_CHOICES = [("Government", "Government"), ("Private", "Private"),("NGO", "NGO"), ("Missionary", "Missionary"), ("None", "None")]
    


   
    surname = models.CharField(max_length=200, default=None)
    othernames = models.CharField(max_length=200, default=None)
    regNo = models.CharField(max_length=200, unique=True)
    dob = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    phone_number = PhoneNumberField()
    email=models.EmailField(max_length=50, unique=True)
    nationality = CountryField()
    district = models.CharField(max_length=100, choices=()) 
    program_level = models.CharField(max_length=100, choices=PROGRAM_LEVEL_CHOICES)
    program = models.CharField(max_length=200, choices=()) 
    exam_center = models.CharField(max_length=200, choices=())
    start_year = models.IntegerField(_('Start Year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    completion_year = models.IntegerField(_('Completion Year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    transcript_status = models.CharField(max_length=30, choices=TRANSCRIPT_CHOICES)
    certificate_status = models.CharField(max_length=30, choices=CERTIFICATE_CHOICES)
    employment_status = models.CharField(max_length=40, choices=EMPLOYMENT_STATUS_CHOICES)
    employment_entity = models.CharField(max_length=40, choices=EMPLOYEMENT_ENTITY_CHOICES)
    
        
    def serialize_nationality(self):
        return str(self.nationality)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('exam_center').choices = get_centers_from_csv('ubiteb\examCenters.csv')
     
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('district').choices = get_districts_from_csv('ubiteb\districts.csv')
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('program').choices = get_programs_from_csv('ubiteb\programs.csv')
    
    

    class Meta:
        ordering = ["surname", "othernames", "regNo"]

    def __str__(self):
        return f"{self.surname} {self.othernames} {self.regNo} ({self.program_level}, {self.program})"

    def get_absolute_url(self):
        return reverse("alumnus-detail", kwargs={"pk": self.pk})


    
    
