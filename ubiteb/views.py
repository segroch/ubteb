from rest_framework import viewsets
from .models import *
from .serializers import *
from django.views.generic import TemplateView
import pandas as pd
import io
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .filters import Alumni_filter
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from .forms import addAlumnus, editAlumnus
import csv
import logging


# Create your views here.
@login_required
def dashboard(request):
    alumnus = Alumni.objects.all().count()
    female_total = Alumni.objects.filter(gender='Female').count()
    male_total = Alumni.objects.filter(gender='Male').count()
    transY_total = Alumni.objects.filter(transcript_status='Received').count()
    transN_total = Alumni.objects.filter(transcript_status='Not Received').count()
    certY_total = Alumni.objects.filter(certificate_status = "Received").count()
    certN_total = Alumni.objects.filter(certificate_status = "Not Received").count()
    empY_stat = Alumni.objects.filter(employment_status = "Employed").count()
    empN_stat = Alumni.objects.filter(employment_status = "Unemployed").count()
    empG_ent = Alumni.objects.filter(employment_entity = "Government").count()
    empP_ent = Alumni.objects.filter(employment_entity  = "Private").count()
    empN_ent = Alumni.objects.filter(employment_entity  = "NGO").count()
    empM_ent = Alumni.objects.filter(employment_entity  = "Missionary").count()
    
    
    return render(request,'home.html',{
        'alumnus':alumnus,
        'female_total':female_total,
        'male_total': male_total,
        'transY_total':transY_total,
        'transN_total':transN_total,
        'certY_total':certY_total,
        'certN_total':certN_total,
        'empY_stat':empY_stat,
        'empN_stat':empN_stat,
        'empG_ent':empG_ent,
        'empP_ent':empP_ent,
        'empN_ent':empN_ent,
        'empM_ent':empM_ent


    })


def add_alumni(request):
    if request.method == "POST":
        form = addAlumnus(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:

        form = addAlumnus()
    return render(request, 'add_alu.html',{'form':form})

            

def edit_alumni(request):
    alumnus = Alumni.objects.all()
    form = editAlumnus(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('al_list')
    return render(request, 'edit_al.html',{'form':form})

def alumni(request):
    alumni = Alumni.objects.all().order_by('id')
    Alumni_filters =Alumni_filter(request.GET, queryset=alumni)
    alumni = Alumni_filters.qs
    total_count = alumni.count()
    return render(request, 'alumni_list.html', {'alumni':alumni,'Alumni_filters':Alumni_filters,'total_count':total_count})

def delete(request):
    pass



class AlumniViewSet(viewsets.ModelViewSet):
    serializer_class = AlumniSerializer
    queryset = Alumni.objects.all()


class CsvUploader(TemplateView):
    template_name ='upload.html'
    logger = logging.getLogger(__name__)

    def post(self, request):
        context = {
            'messages': []
        }

        csv_file = request.FILES['csv_file']

        try:
            self.process_csv_file(csv_file)
            context['messages'].append('CSV file uploaded successfully.')
        except Exception as e:
            context['exceptions_raised'] = e
            self.logger.exception("Error occurred while processing CSV record.")  # Add this line to log the exception

        return render(request, self.template_name, context)

    def process_csv_file(self, csv_file):
        reader = csv.DictReader(csv_file.read().decode('utf-8').splitlines())

        for record in reader:
            try:
                alumni = Alumni.objects.create(
                    surname=record['surname'],
                    othernames=record['othernames'],
                    regNo=record['regNo'],
                    dob=record['dob'],
                    gender=record['gender'],
                    phone_number=record['phone_number'],
                    email=record['email'],
                    nationality=record['nationality'],
                    district=record['district'],
                    program_level=record['program_level'],
                    program=record['program'],
                    exam_center=record['exam_center'],
                    start_year=record['start_year'],
                    completion_year=record['completion_year'],
                    transcript_status=record['transcript_status'],
                    certificate_status=record['certificate_status'],
                    employment_status=record['employment_status'],
                    employment_entity=record['employment_entity'],
                )
                print(f"Created alumni record: {alumni}")
            except Exception as e:
                print(e)
                #Handle exceptions appropriately (e.g., log them, display error messages, etc.)

