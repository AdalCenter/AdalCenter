from modeltranslation.translator import translator, TranslationOptions
from .models import Contact, Address, AboutUs, OurAchievement, OurGoalsAndObjectives, OurTeam, FAQ, Review

class ContactTranslationOptions(TranslationOptions):
    fields = ('title', 'value')  # Укажите поля для перевода

class AddressTranslationOptions(TranslationOptions):
    fields = ('title', 'address')  # Укажите поля для перевода

class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')  # Укажите поля для перевода

class OurAchievementTranslationOptions(TranslationOptions):
    fields = ('title', 'text')  # Укажите поля для перевода

class OurGoalsAndObjectivesTranslationOptions(TranslationOptions):
    fields = ('title', 'text')  # Укажите поля для перевода

class OurTeamTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'speciality')  # Укажите поля для перевода

class FAQTranslationOptions(TranslationOptions):
    fields = ('title', 'text')  # Укажите поля для перевода

class ReviewTranslationOptions(TranslationOptions):
    fields = ('fullname', 'company_and_position_in_it', 'text')  # Укажите поля для перевода

# Регистрация моделей
translator.register(Contact, ContactTranslationOptions)
translator.register(Address, AddressTranslationOptions)
translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(OurAchievement, OurAchievementTranslationOptions)
translator.register(OurGoalsAndObjectives, OurGoalsAndObjectivesTranslationOptions)
translator.register(OurTeam, OurTeamTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
translator.register(Review, ReviewTranslationOptions)
