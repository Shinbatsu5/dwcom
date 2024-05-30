from django.contrib import admin
from.models import Categories,Partners

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']

class PartnersAdmin(admin.ModelAdmin):
    list_display = ['category', ]

admin.site.register(Categories,  CategoriesAdmin)
admin.site.register(Partners, PartnersAdmin)


