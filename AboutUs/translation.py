from modeltranslation.translator import translator, TranslationOptions
from .models import Contact, Address, AboutUs, OurAchievement, OurGoalsAndObjectives, OurTeam, FAQ, Review


class ContactTranslationOptions(TranslationOptions):
    fields = ('title', 'value')

class AddressTranslationOptions(TranslationOptions):
    fields = ('title', 'address')

class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

class OurAchievementTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

class OurGoalsAndObjectivesTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

class OurTeamTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'speciality')

class FAQTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

class ReviewTranslationOptions(TranslationOptions):
    fields = ('fullname', 'company_and_position_in_it', 'text')

translator.register(Contact, ContactTranslationOptions)
translator.register(Address, AddressTranslationOptions)
translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(OurAchievement, OurAchievementTranslationOptions)
translator.register(OurGoalsAndObjectives, OurGoalsAndObjectivesTranslationOptions)
translator.register(OurTeam, OurTeamTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
translator.register(Review, ReviewTranslationOptions)
