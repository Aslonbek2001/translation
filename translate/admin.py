from django.contrib import admin
from .models import Stars, FAQ


class StartModelAdmin(admin.ModelAdmin):
    list_display = ('stars', 'comment')
    list_display_links = ('stars', 'comment')
    list_filter = ('stars', 'comment')


class FAQAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'question', 'answer')
    list_display_links = ('full_name', 'question')
    list_filter = ('full_name', 'question')

admin.site.register(Stars, StartModelAdmin)
admin.site.register(FAQ, FAQAdmin)