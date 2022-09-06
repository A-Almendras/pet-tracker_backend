# Generated by Django 4.1 on 2022-09-06 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('animal_group', models.CharField(choices=[('mammal', 'Mammal'), ('bird', 'Bird'), ('fish', 'Fish'), ('reptile', 'Reptile'), ('amphibian', 'Amphibian'), ('other', 'Other')], max_length=100)),
                ('animal_kind', models.CharField(max_length=100)),
                ('dob', models.CharField(help_text='<em>MM-DD-YYYY</em>', max_length=100)),
                ('gotcha_date', models.DateField()),
                ('age', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('vet', models.CharField(max_length=100)),
                ('appt_date', models.DateField()),
                ('visit_reason', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='pettracker.pet')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='pettracker.user'),
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observations', to='pettracker.pet')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('vet', 'Vet'), ('food', 'Food'), ('toys', 'Toys'), ('apparel', 'Apparel'), ('medical', 'Medical'), ('other', 'Other')], max_length=100)),
                ('date', models.DateField()),
                ('amount', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='pettracker.pet')),
            ],
        ),
    ]
