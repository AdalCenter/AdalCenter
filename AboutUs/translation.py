from modeltranslation.translator import translator, TranslationOptions
from .models import Contact, Address, Partner, Client, AboutUs, OurAchievement, OurGoalsAndObjectives, OurTeam, FAQ, Review, ProcessOfObtainingCertificate, OurIndicators, RatingAndHowYouHeardAboutOurSite, SocialNetwork, MainPhoneNumber, OurSites, MobileAppUrl, SuggestionsOrComplaints

class ContactTranslationOptions(TranslationOptions):
    fields = ('title', 'value',)

class AddressTranslationOptions(TranslationOptions):
    fields = ('title', 'address',)

class PartnerTranslationOptions(TranslationOptions):
    fields = ('url',)

class ClientTranslationOptions(TranslationOptions):
    fields = ('url',)

class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

class OurAchievementTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

class OurGoalsAndObjectivesTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

class OurTeamTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'speciality', 'description',)

class FAQTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

class ReviewTranslationOptions(TranslationOptions):
    fields = ('fullname', 'company_and_position_in_it', 'text',)

class ProcessOfObtainingCertificateTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

class OurIndicatorsTranslationOptions(TranslationOptions):
    fields = ('year_of_foundation', 'number_of_domestic_enterprises', 'number_offoreign_enterprises', 'number_of_professionals',)

class RatingAndHowYouHeardAboutOurSiteTranslationOptions(TranslationOptions):
    fields = ('social_network',)

class SocialNetworkTranslationOptions(TranslationOptions):
    fields = ('url',)

class MainPhoneNumberTranslationOptions(TranslationOptions):
    fields = ('number',)

class OurSitesTranslationOptions(TranslationOptions):
    fields = ('site_name',)

class MobileAppUrlTranslationOptions(TranslationOptions):
    fields = ('google_play', 'app_store',)

class SuggestionsOrComplaintsTranslationOptions(TranslationOptions):
    fields = ('whatsapp_url', 'telegram_url',)

translator.register(Contact, ContactTranslationOptions)
translator.register(Address, AddressTranslationOptions)
translator.register(Partner, PartnerTranslationOptions)
translator.register(Client, ClientTranslationOptions)
translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(OurAchievement, OurAchievementTranslationOptions)
translator.register(OurGoalsAndObjectives, OurGoalsAndObjectivesTranslationOptions)
translator.register(OurTeam, OurTeamTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
translator.register(Review, ReviewTranslationOptions)
translator.register(ProcessOfObtainingCertificate, ProcessOfObtainingCertificateTranslationOptions)
translator.register(OurIndicators, OurIndicatorsTranslationOptions)
translator.register(RatingAndHowYouHeardAboutOurSite, RatingAndHowYouHeardAboutOurSiteTranslationOptions)
translator.register(SocialNetwork, SocialNetworkTranslationOptions)
translator.register(MainPhoneNumber, MainPhoneNumberTranslationOptions)
translator.register(OurSites, OurSitesTranslationOptions)
translator.register(MobileAppUrl, MobileAppUrlTranslationOptions)
translator.register(SuggestionsOrComplaints, SuggestionsOrComplaintsTranslationOptions)
