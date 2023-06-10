import django_filters
from .models import Alumni
from ubiteb.utils import get_programs_from_csv

class Alumni_filter(django_filters.FilterSet):


    class Meta: 
        model = Alumni
        fields = ['surname', 'regNo', 'program', 'gender']