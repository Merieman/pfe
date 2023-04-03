from django.shortcuts import render, redirect
from .models import *
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.db.models import Q
from django import forms
from .forms import candidateformm
from django.http import JsonResponse



def home(request):
    companyC=Company.objects.all()
    candidateC=Candidate.objects.all()
    offerO=Offer.objects.all()
    if companyC.count()==0:
        company_count=0
    else:
        company_count= companyC.count()
        
    if candidateC.count()==0:
        candidate_count=0
    else:
        candidate_count= candidateC.count()

    if offerO.count()==0:
        offer_count=0
    else:
        offer_count= offerO.count()

    context={
        "company_count":company_count,
        "candidate_count":candidate_count,
        "offer_count":offer_count
    }
    return render(request, 'index.html', context)

def get_postulation (request):
    postulationC=Postulation.objects.all()
    candidateC=Candidate.objects.all()
    offerO=Offer.objects.all()
    context={
        "postulation":postulationC,
        "candidate":candidateC,
        "offer":offerO
    }
    return render (request, 'Agence/postulation.html', context)
def get_candidate (request):
    candidateC=Candidate.objects.all()
    fieldcandidate=candidateformm
    context={
        "candidate":candidateC,
        "field":fieldcandidate
    }
    return render (request, 'Agence/candidate.html', context)

def get_company (request):
    companyC=Company.objects.all()
    
    context={
        "company":companyC,
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
    columns = ['id_candidate', 'expertise_field','id','field'] 
    order_columns = ['id_candidate', 'expertise_field','id','field'] 

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
class PostulationJson(BaseDatatableView):
    model = Postulation
    columns = ['id', 'candidate', 'offer', 'application_date', 'acceptation']
    order_columns = ['id', 'candidate', 'offer', 'application_date', 'acceptation']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(candidate__name__istartswith=search) | Q(offer__name__istartswith=search))

        # more advanced example using extra parameters
        filter_candidate = self.request.GET.get('candidate', None)
        filter_offer = self.request.GET.get('offer', None)
        filter_acceptation = self.request.GET.get('acceptation', None)

        if filter_candidate:
            qs = qs.filter(candidate__id=filter_candidate)
        if filter_offer:
            qs = qs.filter(offer__id=filter_offer)
        if filter_acceptation:
            qs = qs.filter(acceptation__icontains=filter_acceptation)

        return qs

    def render_column(self, row, column):
        # We want to render candidate and offer as custom columns
        if column == 'candidate':
            return row.candidate.name
        elif column == 'offer':
            return row.offer.name
        else:
            return super(PostulationJson, self).render_column(row, column)

    def get(self, request, *args, **kwargs):
        # Override get method to return JSON response instead of HTML
        self.process_request(request)
        self.prep_query()
        self.get_ordering()
        self.set_unfiltered_length()
        self.set_filtered_length()
        data = []
        for item in self.get_queryset():
            data.append([self.render_column(item, column) for column in self.columns])
        return JsonResponse({
            'draw': self.draw,
            'recordsTotal': self.unfiltered_length,
            'recordsFiltered': self.filtered_length,
            'data': data,
        })