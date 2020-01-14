from django.contrib import admin
from .models import Menu, Item, Ingredient


admin.site.register(Item)
admin.site.register(Ingredient)

class MenuAdmin(admin.ModelAdmin):
    list_display = ['season','created_date','expiration_date']
    search_fields = ['season']


admin.site.register(Menu, MenuAdmin)
