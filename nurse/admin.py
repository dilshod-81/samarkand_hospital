from django.contrib import admin
from .models import People

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('familiyasi', 'ismi', 'sharifi', 'tugilgan_kuni', 'address', 'passport', 'pinfl', 'telefon_raqami', 'ovqatlanish_turi', 'jismoniy_faolligi', 'zararli_odat', 'vazn', 'buy', 'tvi', 'tashhisi', 'salomatlik_guruhi', 'soglamlashtirish', 'muassasa_nomi', 'davolash_chorak', 'xatlov_sana')
    search_fields = ('familiyasi', 'ismi', 'sharifi', 'passport', 'pinfl', 'telefon_raqami')
    list_filter = ('ovqatlanish_turi', 'jismoniy_faolligi', 'zararli_odat', 'salomatlik_guruhi', 'soglamlashtirish', 'davolash_chorak')

    fieldsets = (
        ('Personal Information', {
            'fields': ('familiyasi', 'ismi', 'sharifi', 'tugilgan_kuni', 'address', 'passport', 'pinfl', 'telefon_raqami')
        }),
        ('Health Information', {
            'fields': ('ovqatlanish_turi', 'jismoniy_faolligi', 'zararli_odat', 'vazn', 'buy', 'tvi', 'tashhisi', 'salomatlik_guruhi', 'soglamlashtirish', 'muassasa_nomi', 'davolash_chorak', 'xatlov_sana')
        }),
    )

    ordering = ('familiyasi', 'ismi')
