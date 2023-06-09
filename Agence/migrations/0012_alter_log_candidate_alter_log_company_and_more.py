# Generated by Django 4.1.6 on 2023-03-22 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agence', '0011_log_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Agence.candidate'),
        ),
        migrations.AlterField(
            model_name='log',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Agence.company'),
        ),
        migrations.AlterField(
            model_name='log',
            name='offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Agence.offer'),
        ),
    ]
