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
    transY_total = Alumni.objects.filter(transcript_status='received').count()
    transN_total = Alumni.objects.filter(transcript_status='not received').count()
    certY_total = Alumni.objects.filter(certificate_status = "received").count()
    certN_total = Alumni.objects.filter(certificate_status = "not received").count()
    empY_stat = Alumni.objects.filter(employment_status = "employed").count()
    empN_stat = Alumni.objects.filter(employment_status = "not employed").count()
    empG_ent = Alumni.objects.filter(employment_entity = "government").count()
    empP_ent = Alumni.objects.filter(employment_entity  = "private").count()
    empN_ent = Alumni.objects.filter(employment_entity  = "ngo").count()
    empM_ent = Alumni.objects.filter(employment_entity  = "missionary").count()
    
    return render(request,'home.html',{
        'alumnus':alumnus,
        'transY_total':transY_total,
        'transN_total':transN_total,
        'certY_total':certY_total,
        'certN_total':certN_total,
        'empY_stat':empY_stat,
        'empN_stat':empN_stat,
        'empG_ent':empG_ent,
        'empP_ent':empP_ent,
        'empN_ent':empN_ent,
        'empM_ent':empM_ent,


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
                    center=record['center'],
                    start_year=record['start_year'],
                    completion_year=record['completion_year'],
                    transcript_status=record['transcript_status'],
                    certificate_status=record['certificate_status'],
                    employment_status=record['employment_status'],
                    employment_entity=record['employment_entity'],
                )
                print(f"Created alumni record: {alumni}")
            except Exception as e:
                #Handle exceptions appropriately (e.g., log them, display error messages, etc.)
                pass

# def upload_csv(request):
#     if request.method == 'POST':
#         csv_file = request.FILES['csv_file']

#         if not csv_file.name.endswith('.csv'):
#             return render(request, 'error.html', {'error': 'Please upload a CSV file.'})

#         csv_data = csv.reader(csv_file.read().decode('utf-8').splitlines())

#         for row in csv_data:
#             surname=row[0],
#             othernames=row[1],
#             regNo=row[2],
#             dob=row[3],
#             gender=row[4],
#             phone_number=row[5]
#             email=row[6],
#             nationality=row[7],
#             district=row[8],
#             program_level=row[9],
#             program=row[10],
#             center=row[11],
#             start_year=row[12],
#             completion_year=row[13],
#             transcript_status=row[14],
#             certificate_status=row[15],
#             employment_status=row[16],
#             employment_entity=row[17],

#             # Create a new instance of YourModel and save it
#             your_model_instance = Alumni(surname=surname, othernames=othernames, regNo=regNo,dob=dob, gender=gender,
#             phone_number=phone_number,email=email,nationality=nationality,district=district,program_level=program_level,program=program,
#             center=center, start_year=start_year, completion_year=completion_year,transcript_status=transcript_status,
#             certificate_status=certificate_status, employment_status=employment_status, employment_entity=employment_entity)
#             your_model_instance.save()

#         return render(request, 'success.html')
#     else:
#         return render(request, 'upload.html')