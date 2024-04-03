from django.contrib import admin
from .models import NewsModel, NewsModelFirst, NewsModelSecond, NewsModelThird
# Register your models here.
admin.site.register(NewsModel)
admin.site.register(NewsModelFirst)
admin.site.register(NewsModelSecond)
admin.site.register(NewsModelThird)