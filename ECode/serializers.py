from rest_framework import serializers
from .models import *


# class CodeTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CodeType
#         fields = ['id', 'code_type']

# class TypeOfOriginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TypeOfOrigin
#         fields = ['id', 'type_of_origin']

class ECodeSerializer(serializers.ModelSerializer):
    # code_type = CodeTypeSerializer(read_only=True)
    # type_of_origin = TypeOfOriginSerializer(read_only=True)

    class Meta:
        model = ECode
        # fields = [
        #     'id', 'code', 'code_name', 'code_type', 'type_of_origin', 
        #     'mini_description', 'code_status', 'description', 'usage'
        # ]
        fields = '__all__'
