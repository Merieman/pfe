# Generated by Django 4.1.6 on 2023-03-30 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agence', '0022_alter_log_candidate_alter_log_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='candidate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='company',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='offer',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
