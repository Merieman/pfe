from django.shortcuts import render, redirect
from .models import *
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.db.models import Q
from django import forms
 

def home(request):
    return render(request, 'index.html')

def get_candidate (request):
    candidateC=Candidate.objects.all()
    context={
        "candidate":candidateC
    }
    return render (request, 'Agence/candidate.html', context)

def get_company (request):
    companyC=Company.objects.all()
    context={
        "company":companyC
    }
    return render (request, 'Agence/company.html', context)

def get_offer (request):
    offerO=Offer.objects.all()
    context={
        "offer":offerO
    }
    return render (request, 'Agence/offer.html', context)

def get_add_candidate (request):
    candidateC=Candidate.objects.all()
    context={
        "candidate":candidateC
    }
    return render (request, 'Agence/add_candidate.html', context)

def save(request):
    # Retrieve form data from POST request
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    birth_date = request.POST.get('birth_date')
    gender = request.POST.get('gender')
    nationality = request.POST.get('nationality')
    address = request.POST.get('address')
    city = request.POST.get('city')
    phone_number = request.POST.get('phone_number')
    email = request.POST.get('email')
    education_level = request.POST.get('education_level')
    driving_license=request.POST.get('driving_license')
    linkedin=request.POST.get('linkedin')
    technical_skills=request.POST.get('technical_skills')
    language_skills=request.POST.get('language_skills')
    social_skills=request.POST.get('social_skills')
    expertise_field=request.POST.get('expertise_field')
    password=request.POST.get('password')
    # Create a new Candidate instance and save it to the database
    Candidate.objects.create(
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date,
        gender=gender,
        nationality=nationality,
        address=address,
        driving_license=driving_license,
        city=city,
        phone_number=phone_number,
        email=email,
        linkedin=linkedin,
        technical_skills=technical_skills,
        language_skills=language_skills,
        social_skills=social_skills,
        expertise_field=expertise_field,
        password=password,
        education_level=education_level,
    )

    # Redirect to the candidate page
    return redirect('candidate')
 


class candidateJson(BaseDatatableView):
    model = Candidate
    columns = ['id_candidate', 'driving_license', 'city', 'technical_skills', 'language_skills' , 'social_skills', 'education_level', 'expertise_field'] 
    order_columns = ['id_candidate', 'driving_license', 'city', 'technical_skills', 'language_skills' , 'social_skills', 'education_level', 'expertise_field'] 
 
    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500
    count = 0
    def render_column(self, row, column):
        # We want to render user as a custom column
   
            return super(candidateJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)

        # more advanced example using extra parameters
        filter_customer = self.request.GET.get('customer', None)

        if filter_customer:
            customer_parts = filter_customer.split(' ')
            qs_params = None
            for part in customer_parts:
                q = Q(customer_firstname__istartswith=part) | Q(customer_lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs
    
class companyJson(BaseDatatableView):
    model = Company
    columns = ['company_id', 'address', 'headquarters', 'business_sector'] 
    order_columns = ['company_id', 'address', 'headquarters', 'business_sector'] 

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):
        # We want to render user as a custom column
        return super(companyJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)

        # more advanced example using extra parameters
        filter_customer = self.request.GET.get('customer', None)

        if filter_customer:
            customer_parts = filter_customer.split(' ')
            qs_params = None
            for part in customer_parts:
                q = Q(customer_firstname__istartswith=part) | Q(customer_lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs
    
class offerJson(BaseDatatableView):
    model = Offer
    columns = ['id', 'title', 'job_type', 'date_cloture', 'description', 'skills', 'experience', 'education_level', 'number_of_positions', 'languages'] 
    order_columns = ['id', 'title', 'job_type', 'date_cloture', 'description', 'skills', 'experience', 'education_level', 'number_of_positions', 'languages']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):
        # We want to render user as a custom column
        return super(offerJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)

        # more advanced example using extra parameters
        filter_customer = self.request.GET.get('customer', None)

        if filter_customer:
            customer_parts = filter_customer.split(' ')
            qs_params = None
            for part in customer_parts:
                q = Q(customer_firstname__istartswith=part) | Q(customer_lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs
