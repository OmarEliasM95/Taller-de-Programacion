# Generated by Django 5.0.7 on 2024-08-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lista', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Precio',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
