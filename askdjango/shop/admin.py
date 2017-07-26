from django.contrib import admin
from .models import Shop, Rating


admin.site.register(Shop)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('shop', 'score')

