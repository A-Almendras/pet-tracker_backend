from pyexpat import model
from unicodedata import name
from django.contrib import admin
from .models import Pet, Expense, Observation, Record


class PetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'user_id'
    )
    list_display_links = ['id', 'user_id']
    list_editable = ['name']
    # list_filter = []

    search_fields = ['user_id']

    class Meta:
        model = Pet


# Register your models here.
# admin.site.register(UserAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Expense)
admin.site.register(Observation)
admin.site.register(Record)
