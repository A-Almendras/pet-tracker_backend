# Generated by Django 4.1.1 on 2022-09-16 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pettracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Vet', 'Vet'), ('Food', 'Food'), ('Toys', 'Toys'), ('Apparel', 'Apparel'), ('Medical', 'Medical'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='pet',
            name='animal_group',
            field=models.CharField(choices=[('Mammal', 'Mammal'), ('Bird', 'Bird'), ('Fish', 'Fish'), ('Reptile', 'Reptile'), ('Amphibian', 'Amphibian'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to=settings.AUTH_USER_MODEL),
        ),
    ]
