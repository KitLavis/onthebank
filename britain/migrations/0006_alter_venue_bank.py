# Generated by Django 4.2 on 2024-04-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('britain', '0005_alter_venue_fictitious'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='bank',
            field=models.CharField(max_length=50),
        ),
    ]
