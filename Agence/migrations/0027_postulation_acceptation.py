# Generated by Django 4.1.6 on 2023-04-01 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agence', '0026_alter_offer_education_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulation',
            name='acceptation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
