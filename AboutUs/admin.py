from django.contrib import admin
from .models import *


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'value')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('title', 'address')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('logo', 'url')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('logo', 'url')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'image')

@admin.register(OurAchievement)
class OurAchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'icon')

@admin.register(OurAchievementCertificateImage)
class OurAchievementCertificateImageAdmin(admin.ModelAdmin):
    list_display = ('image',)

@admin.register(OurGoalsAndObjectives)
class OurGoalsAndObjectivesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'speciality', 'description')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

@admin.register(Boycott)
class BoycottAdmin(admin.ModelAdmin):
    list_display = ('company_logo')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars', 'text')

@admin.register(ProcessOfObtainingCertificate)
class ProcessOfObtainingCertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon', 'backgrount_image')

@admin.register(OurIndicators)
class OurIndicatorsAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(RatingAndHowYouHeardAboutOurSite)
class RatingAndHowYouHeardAboutOurSiteAdmin(admin.ModelAdmin):
    list_display = ('stars', 'social_network')
