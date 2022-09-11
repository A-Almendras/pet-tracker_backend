from django.contrib import admin
from .models import Pet, Expense, Observation, Record


class PetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'user_id'
    )


# Register your models here.
# admin.site.register(UserAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Expense)
admin.site.register(Observation)
admin.site.register(Record)
