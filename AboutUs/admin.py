from django.contrib import admin
from .models import (
    Contact, Address, Partner, AboutUs, OurAchievement,
    OurGoalsAndObjectives, OurAchievementCertificateImage,
    OurTeam, FAQ, BlackListCompany
)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'value')
    search_fields = ('title', 'value')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('title', 'address')
    search_fields = ('title', 'address')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('logo', 'url')
    search_fields = ('url',)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'text')

@admin.register(OurAchievement)
class OurAchievementAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'text')

@admin.register(OurGoalsAndObjectives)
class OurGoalsAndObjectivesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'text')

@admin.register(OurAchievementCertificateImage)
class OurAchievementCertificateImageAdmin(admin.ModelAdmin):
    list_display = ('image',)

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'speciality')
    search_fields = ('first_name', 'last_name', 'speciality', 'description')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'text')

@admin.register(BlackListCompany)
class BlackListCompanyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')
