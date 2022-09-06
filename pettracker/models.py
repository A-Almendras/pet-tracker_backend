from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    # user_image =

    def __str__(self):
        return self.username


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
    dob = models.CharField(max_length=100, help_text='<em>MM-DD-YYYY</em>')
    gotcha_date = models.DateField()
    age = models.PositiveIntegerField()
    # pet_image =

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
    date = models.DateField()
    amount = models.PositiveIntegerField()
    description = models.TextField()
    # expense_image =

    def __str__(self):
        return self.category


class Observation(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE,
                            related_name='observations')
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    # obvs_image =

    def __str__(self):
        return self.title


class Record(models.Model):
    pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name='records')
    clinic_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    vet = models.CharField(max_length=100)
    appt_date = models.DateField()
    visit_reason = models.CharField(max_length=100)
    comment = models.TextField()
    # record_image =

    def __str__(self):
        return self.visit_reason
