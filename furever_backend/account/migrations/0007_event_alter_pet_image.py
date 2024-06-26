# Generated by Django 5.0.6 on 2024-05-30 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_pet_shelterprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
