from django.contrib import admin
from .models import Moeda
# Register your models here.


class MoedaAdmin(admin.ModelAdmin):
    list_display = ('pais_nome', 'pais_codigo', 'moeda_codigo', 'moeda_swift')


admin.site.register(Moeda, MoedaAdmin)
