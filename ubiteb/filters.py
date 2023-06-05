import django_filters
from .models import Alumni

class Alumni_filter(django_filters.FilterSet):
    class Meta: 
        model = Alumni
        fields = ['surname', 'regNo', 'program', ]