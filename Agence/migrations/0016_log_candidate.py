# Generated by Django 4.1.7 on 2023-03-28 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agence', '0015_alter_postulation_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Agence.candidate'),
        ),
    ]
