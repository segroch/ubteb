from rest_framework import serializers
from .models import *

class AlumniSerializer(serializers.ModelSerializer):
    # nationality = serializers.SerializerMethodField()

    def get_nationlity(self, obj):
        return obj.serialize_nationality()

    class Meta:
        model = Alumni
        fields = '__all__'
        