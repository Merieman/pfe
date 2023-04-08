from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from model_utils.models import TimeStampedModel, SoftDeletableModel
from model_utils import FieldTracker
from model_utils.fields import StatusField
from django.contrib.auth.password_validation import validate_password


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    business_sector = models.CharField(max_length=100)
    size = models.IntegerField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    headquarters = models.CharField(max_length=100)
    website = models.URLField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email_address = models.EmailField()
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=128, validators=[validate_password])
    tracker = FieldTracker()
    def __str__(self) :
        return self.company_name


class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    field = models.CharField(max_length=100)
    description = models.TextField()
    skills = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    education_level = models.CharField(max_length=50, blank=True, null=True)
    workplace = models.CharField(max_length=100)
    contract_type = models.CharField(max_length=50)
    contract_duration = models.CharField(max_length=100, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    number_of_positions = models.IntegerField(blank=True, null=True)
    languages = models.CharField(max_length=100, blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    tracker = FieldTracker()
    def __str__(self) :
        return self.title
        
        



class Candidate(models.Model):
    id_candidate = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    driving_license = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    linkedin = models.URLField(blank=True, null=True)
    technical_skills = models.TextField(blank=True, null=True)
    language_skills = models.TextField(blank=True, null=True)
    social_skills = models.TextField(blank=True, null=True)
    education_level = models.CharField(max_length=50, blank=True, null=True)
    expertise_field = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=128, validators=[validate_password])
    tracker = FieldTracker()
    def __str__(self) :
        return self.first_name +' ' + self.last_name
    


class Log(models.Model):
    id_log = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    candidate =  models.CharField(max_length=100, blank=True, null=True)
    offer =  models.CharField(max_length=100, blank=True, null=True)
    company =  models.CharField(max_length=100, blank=True, null=True)
    admin_email = models.EmailField()

    def save(self, *args, **kwargs):
        # Récupérer l'administrateur actuel
        admin = User.objects.filter(is_superuser=True).first()

        # Remplir les champs manquants
        self.admin_email = admin.email
        super(Log, self).save(*args, **kwargs)

    def log_create(sender, instance, **kwargs):
        if isinstance(instance, Candidate):
            if instance.tracker.previous('email') is not None:
                return
            action = 'create_candidate'
            description = f"New candidate {instance.first_name} {instance.last_name} ({instance.email}) created"
        elif isinstance(instance, Offer):
            if instance.tracker.previous('title') is not None:
                return
            action = 'create_offer'
            description = f"New offer {instance.title} ({instance.company.company_name}) created"
        elif isinstance(instance, Company):
            if instance.tracker.previous('email_address') is not None:
                return
            action = 'create_company'
            description = f"New company {instance.company_name} created"
        else:
            return

        Log.objects.create(
            action=action,
            description=description,
            candidate=instance.id_candidate if isinstance(instance, Candidate) else None,
            offer=instance.id if isinstance(instance, Offer) else None,
            company=instance.company_id if isinstance(instance, Company) else None,
        )

    def log_update(sender, instance, **kwargs):
        if instance.pk is None:  # Vérifier si l'instance a déjà été créée
            return
        if isinstance(instance, Candidate):
            if instance.tracker.previous('email') is None:
                return
            action = 'update_candidate'
            description = f"Candidate {instance.first_name} {instance.last_name} ({instance.email}) updated: "

            # Créer une liste de tous les champs qui ont été modifiés
            updated_fields = instance.tracker.changed()

            # Ajouter chaque champ modifié à la description détaillée
            for field in updated_fields:
                old_value = instance.tracker.previous(field)
                new_value = getattr(instance, field)
                description += f"\n  - {field}: {old_value} -> {new_value}"
        elif isinstance(instance, Offer):
            if instance.tracker.previous('title') is None:
                return
            action = 'update_offer'
            description = f"Offer {instance.title} ({instance.company.company_name}) updated: "

            # Créer une liste de tous les champs qui ont été modifiés
            updated_fields = instance.tracker.changed()

            # Ajouter chaque champ modifié à la description détaillée
            for field in updated_fields:
                old_value = instance.tracker.previous(field)
                new_value = getattr(instance, field)
                description += f"\n  - {field}: {old_value} -> {new_value}"
        elif isinstance(instance, Company):
            if instance.tracker.previous('email_address') is None:
                return
            action = 'update_company'
            description = f"Company {instance.company_name} updated: "

            # Créer une liste de tous les champs qui ont été modifiés
            updated_fields = instance.tracker.changed()

            # Ajouter chaque champ modifié à la description détaillée
            for field in updated_fields:
                old_value = instance.tracker.previous(field)
                new_value = getattr(instance, field)
                description += f"\n  - {field}: {old_value} -> {new_value}"
        else:
            return

        Log.objects.create(
            action=action,
            description=description,
            candidate=instance.id_candidate if isinstance(instance, Candidate) else None,
            offer=instance.id if isinstance(instance, Offer) else None,
            company=instance.company_id if isinstance(instance, Company) else None,
        )

  

    def log_delete(sender, instance, **kwargs):
        if isinstance(instance, Candidate):
            action = 'delete_candidate'
            description = f"Candidate {instance.first_name} {instance.last_name} ({instance.email}) deleted"
        elif isinstance(instance, Offer):
            action = 'delete_offer'
            description = f"Offer {instance.title} ({instance.company.company_name}) deleted"
        elif isinstance(instance, Company):
            action = 'delete_company'
            description = f"Company {instance.company_name} deleted"
        else:
            return

        Log.objects.create(
            action=action,
            description=description,
            candidate=instance.id_candidate if isinstance(instance, Candidate) else None,
            offer=instance.id if isinstance(instance, Offer) else None,
            company=instance.company_id if isinstance(instance, Company) else None,
        )

    # Connecter les fonctions de rappel aux signaux correspondants
    models.signals.post_save.connect(log_create)
    models.signals.post_save.connect(log_update)
    models.signals.post_delete.connect(log_delete)


class Postulation(models.Model):
    candidate = models.ForeignKey(
        Candidate, on_delete=models.SET_DEFAULT, default=-1)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, default=-1)
    application_date = models.DateField(auto_now_add=True)
    acceptation = models.CharField(max_length=50,blank=True, null=True)
