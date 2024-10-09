from rest_framework import serializers
from .models import *


class ECodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECode
        fields = '__all__'
