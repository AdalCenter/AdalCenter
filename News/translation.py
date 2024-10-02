from modeltranslation.translator import translator, TranslationOptions
from .models import News, NewsPhoto

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description')

class NewsPhotoTranslationOptions(TranslationOptions):
    fields = ('photo',)

translator.register(News, NewsTranslationOptions)
translator.register(NewsPhoto, NewsPhotoTranslationOptions)
