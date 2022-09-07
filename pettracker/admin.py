from django.contrib import admin
from .models import User, Pet, Expense, Observation, Record

# Register your models here.
# admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Expense)
admin.site.register(Observation)
admin.site.register(Record)
