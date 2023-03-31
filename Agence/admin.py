from django.contrib import admin

from Agence.models import Company, Offer, Candidate

# Register your models here.
admin.site.register(Offer)
admin.site.register(Company)
admin.site.register(Candidate)

