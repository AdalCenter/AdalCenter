from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *
from .translation import *

@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
    list_display = ('title', 'value')
    search_fields = ('title', 'value')

@admin.register(Address)
class AddressAdmin(TranslationAdmin):
    list_display = ('title', 'address')
    search_fields = ('title', 'address')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('url',)
    search_fields = ('url',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('url',)
    search_fields = ('url',)

@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    list_display = ('title', 'text')
    search_fields = ('title', 'text')

@admin.register(OurAchievement)
class OurAchievementAdmin(TranslationAdmin):
    list_display = ('title', 'text')
    search_fields = ('title', 'text')

@admin.register(OurAchievementCertificateImage)
class OurAchievementCertificateImageAdmin(admin.ModelAdmin):
    list_display = ('image',)

@admin.register(OurGoalsAndObjectives)
class OurGoalsAndObjectivesAdmin(TranslationAdmin):
    list_display = ('title', 'text')
    search_fields = ('title', 'text')

@admin.register(OurTeam)
class OurTeamAdmin(TranslationAdmin):
    list_display = ('first_name', 'last_name', 'speciality')
    search_fields = ('first_name', 'last_name', 'speciality')

@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ('title', 'text')
    search_fields = ('title', 'text')

@admin.register(Boycott)
class BoycottAdmin(admin.ModelAdmin):
    list_display = ('company_logo',)

@admin.register(Review)
class ReviewAdmin(TranslationAdmin):
    list_display = ('fullname', 'company_and_position_in_it', 'text')
    search_fields = ('fullname', 'company_and_position_in_it', 'text')

@admin.register(ProcessOfObtainingCertificate)
class ProcessOfObtainingCertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

@admin.register(OurIndicators)
class OurIndicatorsAdmin(admin.ModelAdmin):
    list_display = ('year_of_foundation', 'number_of_domestic_enterprises', 'number_offoreign_enterprises', 'number_of_professionals')

@admin.register(RatingAndHowYouHeardAboutOurSite)
class RatingAndHowYouHeardAboutOurSiteAdmin(admin.ModelAdmin):
    list_display = ('stars', 'social_network')

@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('url',)
    search_fields = ('url',)

@admin.register(MainPhoneNumber)
class MainPhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number',)

@admin.register(OurSites)
class OurSitesAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_url')
    search_fields = ('site_name', 'site_url')

@admin.register(MobileAppUrl)
class MobileAppUrlAdmin(admin.ModelAdmin):
    list_display = ('google_play', 'app_store')

@admin.register(SuggestionsOrComplaints)
class SuggestionsOrComplaintsAdmin(admin.ModelAdmin):
    list_display = ('whatsapp_url', 'telegram_url')
