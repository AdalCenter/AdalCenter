from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (
    Contact, Address, Partner, Client, AboutUs, OurAchievement,
    OurAchievementCertificateImage, OurGoalsAndObjectives, FAQ, Review,
    ProcessOfObtainingCertificate, OurTeam, Boycott, OurIndicators,
    RatingAndHowYouHeardAboutOurSite, SocialNetwork, MainPhoneNumber,
    OurSites, MobileAppUrl, SuggestionsOrComplaints
)


@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
    list_display = ('title', 'value')


@admin.register(Address)
class AddressAdmin(TranslationAdmin):
    list_display = ('title', 'address')


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    list_display = ('title', 'text', 'image')


@admin.register(OurAchievement)
class OurAchievementAdmin(TranslationAdmin):
    list_display = ('title', 'text', 'icon')


@admin.register(OurGoalsAndObjectives)
class OurGoalsAndObjectivesAdmin(TranslationAdmin):
    list_display = ('title', 'text')


@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ('title', 'text')


@admin.register(Review)
class ReviewAdmin(TranslationAdmin):
    list_display = ('fullname', 'company_and_position_in_it', 'text', 'profile_photo')


@admin.register(ProcessOfObtainingCertificate)
class ProcessOfObtainingCertificateAdmin(TranslationAdmin):
    list_display = ('title', 'description', 'icon', 'background_image')


@admin.register(OurTeam)
class OurTeamAdmin(TranslationAdmin):
    list_display = ('first_name', 'last_name', 'speciality', 'description', 'image')


@admin.register(OurSites)
class OurSitesAdmin(TranslationAdmin):
    list_display = ('site_name', 'site_url', 'icon')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('url', 'logo')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('url', 'logo')


@admin.register(OurAchievementCertificateImage)
class OurAchievementCertificateImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Boycott)
class BoycottAdmin(admin.ModelAdmin):
    list_display = ('company_logo',)


@admin.register(OurIndicators)
class OurIndicatorsAdmin(admin.ModelAdmin):
    list_display = (
        'year_of_foundation', 'number_of_domestic_enterprises',
        'number_offoreign_enterprises', 'number_of_professionals'
    )


@admin.register(RatingAndHowYouHeardAboutOurSite)
class RatingAndHowYouHeardAboutOurSiteAdmin(admin.ModelAdmin):
    list_display = ('stars', 'social_network')


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('icon', 'url')


@admin.register(MainPhoneNumber)
class MainPhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number',)


@admin.register(MobileAppUrl)
class MobileAppUrlAdmin(admin.ModelAdmin):
    list_display = ('qr_code', 'google_play', 'app_store')


@admin.register(SuggestionsOrComplaints)
class SuggestionsOrComplaintsAdmin(admin.ModelAdmin):
    list_display = ('telegram_qr_code', 'whatsapp_qr_code', 'whatsapp_url', 'telegram_url')
