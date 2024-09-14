from rest_framework import serializers
from .models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class BlackListCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackListCompany
        fields = '__all__'


class OurAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurAchievement
        fields = '__all__'


class OurGoalsAndObjectivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurGoalsAndObjectives
        fields = '__all__'


class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = '__all__'


class OurAchievementCertificateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurAchievementCertificateImage
        fields = '__all__'
