from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .filters import Alumni_filter
from .forms import addAlumnus, editAlumnus

# Create your views here.
@login_required
def home (request):
    return render(request, 'home.html')


def dashboard(request):
    alumnus = Alumni.objects.all().count()
    transY_total = Alumni.objects.filter(transcript_status='received').count()
    transN_total = Alumni.objects.filter(transcript_status='not received').count()
    certY_total = Alumni.objects.filter(certificate_status = "received").count()
    certN_total = Alumni.objects.filter(certificate_status = "not received").count()
    empY_stat = Alumni.objects.filter(employment_status = "yes").count()
    empN_stat = Alumni.objects.filter(employment_status = "no").count()
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
    return render(request, 'alumni_list.html', {'alumni':alumni,'Alumni_filters':Alumni_filters,})

def delete(request):
    pass
