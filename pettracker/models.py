from django.db import models
from django.conf import settings

# Create your models here.


# class User(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     location = models.CharField(max_length=100, blank=True)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=500)
#     # user_image =

#     def __str__(self):
#         return self.username


User = settings.AUTH_USER_MODEL


# Each class of this is an instance (as an object) of the Pet class
class Pet(models.Model):
    GROUP_CHOICES = (
        ('mammal', 'Mammal'),
        ('bird', 'Bird'),
        ('fish', 'Fish'),
        ('reptile', 'Reptile'),
        ('amphibian', 'Amphibian'),
        ('other', 'Other')
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=100)
    animal_group = models.CharField(max_length=100, choices=GROUP_CHOICES)
    animal_kind = models.CharField(max_length=100)
    dob = models.DateField(help_text='<em>YYYY-MM-DD</em>',
                           blank=True, null=True, verbose_name='DOB')
    gotcha_date = models.DateField(help_text='<em>YYYY-MM-DD</em>')
    age = models.PositiveIntegerField(blank=True, null=True)
    # pet_image = models.CharField(max_length=None)

    def __str__(self):
        return self.name


class Expense(models.Model):
    CATEGORY_CHOICES = (
        ('vet', 'Vet'),
        ('food', 'Food'),
        ('toys', 'Toys'),
        ('apparel', 'Apparel'),
        ('medical', 'Medical'),
        ('other', 'Other'),
    )
    pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name='expenses')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    date = models.DateField(
        help_text='<em>YYYY-MM-DD</em>', blank=True, null=True)
    amount = models.FloatField(help_text='<em>Currency in USD</em>')
    description = models.TextField(blank=True)
    # expense_image = models.CharField(max_length=None)
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # time_stamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.category


class Observation(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE,
                            related_name='observations')
    title = models.CharField(max_length=100, blank=True)
    date = models.DateField(help_text='<em>YYYY-MM-DD</em>', blank=True)
    description = models.TextField(blank=True)
    # obvs_image = mmodels.CharField(max_length=None)
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # time_stamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title


class Record(models.Model):
    pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name='records')
    clinic_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    vet = models.CharField(max_length=100, blank=True)
    appt_date = models.DateField(
        help_text='<em>YYYY-MM-DD</em>', blank=True, null=True)
    visit_reason = models.CharField(max_length=100, blank=True)
    comment = models.TextField(blank=True)
    # record_image = models.CharField(max_length=None)
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # time_stamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.visit_reason
