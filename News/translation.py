from modeltranslation.translator import translator, TranslationOptions
from .models import News, NewsPhoto

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'address',)

class NewsPhotoTranslationOptions(TranslationOptions):
    fields = ()

translator.register(News, NewsTranslationOptions)
translator.register(NewsPhoto, NewsPhotoTranslationOptions)
