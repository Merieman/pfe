from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages


def home(request):
    companyC = Company.objects.all()
    candidateC = Candidate.objects.all()
    offerO = Offer.objects.all()
    if companyC.count() == 0:
        company_count = 0
    else:
        company_count = companyC.count()

    if candidateC.count() == 0:
        candidate_count = 0
    else:
        candidate_count = candidateC.count()

    if offerO.count() == 0:
        offer_count = 0
    else:
        offer_count = offerO.count()

    context = {
        "company_count": company_count,
        "candidate_count": candidate_count,
        "offer_count": offer_count
    }
    return render(request, 'index.html', context)


def L_c_c(request):
    return render(request, 'com_or_can_L.html')


def S_c_c(request):
    return render(request, 'com_or_can_S.html')


def about_us(request):
    return render(request, 'about_us.html', )


def about_us_can(request, id):
    obj = get_object_or_404(Candidate, pk=id)
    context = {
        "obj": obj,
    }
    return render(request, 'about_us_can.html', context)


def about_us_com(request):
    return render(request, 'about_us_com.html')


def sign_can(request):
    candidateC = Candidate.objects.all()

    context = {
        "candidate": candidateC,
    }
    return render(request, 'signup_can.html', context)


def sign_com(request):
    companyC = Company.objects.all()

    context = {
        "company": companyC,
    }
    return render(request, 'signup_com.html', context)


def log_com(request):
    companyC = Company.objects.all()

    context = {
        "company": companyC,
    }
    return render(request, 'login_com.html', context)


def log_can(request):
    candidateC = Candidate.objects.all()

    context = {
        "candidate": candidateC,
    }
    return render(request, 'login_can.html', context)


def save_login_can(request):

    email = request.POST.get('email')
    password = request.POST.get('password')
    # Create a new Candidate instance and save it to the database

    obj = Candidate.objects.filter(email=email).first()
    if obj:
        if obj.password == password:
            redirect_url = reverse('home_can', args=(obj.pk,))
            return redirect(redirect_url)
        else:
            messages.error(request, 'the password is incorrect')
            return render(request, 'login_can.html', {'email': email, 'password': password})
    else:
        messages.error(request, 'the email is incorrect')
        return render(request, 'login_can.html', {'email': email, 'password': password})


def save_login_com(request):

    email = request.POST.get('email')
    password = request.POST.get('password')
    # Create a new Candidate instance and save it to the database

    obj = Company.objects.filter(email_address=email).first()
    if obj:
        if obj.password == password:
            redirect_url = reverse('home_com', args=(obj.pk,))
            return redirect(redirect_url)
        else:
            messages.error(request, 'the password is incorrect')
            return render(request, 'login_com.html', {'email': email, 'password': password})
    else:
        messages.error(request, 'the email is incorrect')
        return render(request, 'login_com.html', {'email': email, 'password': password})


def home_a(request):
    num_cards = int(request.GET.get('num_cards', 0))
    all_offer = Offer.objects.all()[num_cards:num_cards+5]

    has_more = Offer.objects.count() > num_cards + 5
    if not has_more:
        show_button = False
    else:
        show_button = True

    context = {
        "my_objects": all_offer,
        "has_more": show_button,
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'my_cards_a.html', context)
    return render(request, 'accueil.html', context)


def list_cand(request, id):
    obj = get_object_or_404(Company, pk=id)

    num_cards = int(request.GET.get('num_cards', 0))
    all_can = Candidate.objects.all()[num_cards:num_cards+5]

    has_more = Candidate.objects.count() > num_cards + 5
    if not has_more:
        show_button = False
    else:
        show_button = True

    context = {
        "obj_can": all_can,
        "has_more": show_button,
        'obj': obj,
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'list_card.html', context)
    return render(request, 'list_can.html', context)


def home_com(request, obj_id):
    obj = get_object_or_404(Company, pk=obj_id)
    offerO = Offer.objects.filter(company=obj_id)
    count_all = 0
    if offerO.count() == 0:
        offer_count = 0
    else:
        offer_count = offerO.count()
        for objo in offerO:
            postP = Postulation.objects.filter(
                offer=objo.id, acceptation='true')
            acc = postP.count()
            count_all += acc

    context = {
        'obj': obj,
        'offer_count': offer_count,
        'count_all': count_all,
        'id': obj_id
    }
    return render(request, 'accueil_com.html', context)


def home_can(request, obj_id):
    obj = get_object_or_404(Candidate, pk=obj_id)

    pst = Postulation.objects.filter(candidate=obj_id)
    off_j = Offer.objects.filter(job_type='job')
    off_i = Offer.objects.filter(job_type='internship')
    count_job = 0
    count_int = 0
    for p in pst:
        for o in off_j:
            if p.offer.pk == o.id:
                count_job += 1
        for a in off_i:
            if p.offer.pk == a.id:
                count_int += 1
    context = {
        'obj': obj,
        'count_int': count_int,
        'count_job': count_job
    }
    return render(request, 'accueil_can.html', context)


def internship_a(request):
    num_cards_int = int(request.GET.get('num_cards_int', 0))
    internship_offer = Offer.objects.filter(job_type='internship')[
        num_cards_int:num_cards_int+5]

    has_more_int = Offer.objects.filter(
        job_type='internship').count() > num_cards_int + 5
    if not has_more_int:
        show_button_int = False
    else:
        show_button_int = True

    context = {
        "my_objects_int": internship_offer,
        "has_more_int": show_button_int
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'cards_int.html', context)
    return render(request, 'internship.html', context)


def internship_can(request, id):
    num_cards_int = int(request.GET.get('num_cards_int', 0))
    obj = get_object_or_404(Candidate, pk=id)

    internship_offer = Offer.objects.filter(job_type='internship')[
        num_cards_int:num_cards_int+5]

    has_more_int = Offer.objects.filter(
        job_type='internship').count() > num_cards_int + 5
    if not has_more_int:
        show_button_int = False
    else:
        show_button_int = True

    context = {
        "my_objects_int": internship_offer,
        "has_more_int": show_button_int,
        "obj": obj
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'card_intc.html', context)
    return render(request, 'internship_can.html', context)


def job_a(request):
    num_cards_job = int(request.GET.get('num_cards_job', 0))
    job_offer = Offer.objects.filter(job_type='job')[
        num_cards_job:num_cards_job+5]

    has_more_job = Offer.objects.filter(
        job_type='job').count() > num_cards_job + 5
    if not has_more_job:
        show_button_job = False
    else:
        show_button_job = True

    context = {
        "my_objects_job": job_offer,
        "has_more_job": show_button_job
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'card_job.html', context)
    return render(request, 'job.html', context)


def job_can(request, id):
    obj = get_object_or_404(Candidate, pk=id)
    num_cards_job = int(request.GET.get('num_cards_job', 0))
    job_offer = Offer.objects.filter(job_type='job')[
        num_cards_job:num_cards_job+5]

    has_more_job = Offer.objects.filter(
        job_type='job').count() > num_cards_job + 5
    if not has_more_job:
        show_button_job = False
    else:
        show_button_job = True

    context = {
        "my_objects_job": job_offer,
        "has_more_job": show_button_job,
        "obj": obj
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'jobc_card.html', context)
    return render(request, 'job_can.html', context)


def app_job(request, id):
    obj = get_object_or_404(Candidate, pk=id)
    num_cards_job = int(request.GET.get('num_cards_job', 0))
    pst = Postulation.objects.filter(
        candidate=id)[num_cards_job:num_cards_job+5]
    off = Offer.objects.filter(job_type='job')

    has_more_job = Postulation.objects.filter(
        candidate=id).count() > num_cards_job + 5
    if not has_more_job:
        show_button_job = False
    else:
        show_button_job = True

    context = {
        "pst": pst,
        "off": off,
        "has_more_job": show_button_job,
        "obj": obj
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'app_card_j.html', context)
    return render(request, 'app_job.html', context)


def app_int(request, id):
    obj = get_object_or_404(Candidate, pk=id)
    num_cards_job = int(request.GET.get('num_cards_job', 0))
    pst = Postulation.objects.filter(
        candidate=id)[num_cards_job:num_cards_job+5]
    off = Offer.objects.filter(job_type='internship')

    has_more_job = Postulation.objects.filter(
        candidate=id).count() > num_cards_job + 5
    if not has_more_job:
        show_button_job = False
    else:
        show_button_job = True

    context = {
        "pst": pst,
        "off": off,
        "has_more_job": show_button_job,
        "obj": obj
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'app_card_i.html', context)
    return render(request, 'app_int.html', context)


def more_info(request, id):
    obj = Offer.objects.get(id=id)
    return render(request, 'more_info.html', {'obj': obj})


def more_infoc(request, id, idf):
    objf = Offer.objects.get(id=idf)
    obj = Candidate.objects.get(id_candidate=id)
    context = {
        "objf": objf,
        "obj": obj
    }
    return render(request, 'more_infoc.html', context)


def pers_info(request, id):
    obj = Candidate.objects.get(id_candidate=id)
    return render(request, 'contact.html', {'obj': obj})


def contact(request):
    return render(request, 'contact.html')


def contact_can(request, id):
    obj = Candidate.objects.get(id_candidate=id)
    context = {'obj': obj}
    return render(request, 'contact_can.html', context)


def contact_com(request):
    return render(request, 'contact_com.html')


def get_postulation(request):
    postulationC = Postulation.objects.all()
    candidateC = Candidate.objects.all()
    offerO = Offer.objects.all()
    context = {
        "postulation": postulationC,
        "candidate": candidateC,
        "offer": offerO
    }
    return render(request, 'Agence/postulation.html', context)


def get_candidate(request):
    candidateC = Candidate.objects.all()
    context = {
        "candidate": candidateC,
    }
    return render(request, 'Agence/candidate.html', context)


def get_company(request):
    companyC = Company.objects.all()

    context = {
        "company": companyC,
    }
    return render(request, 'Agence/company.html', context)


def get_offer(request):
    offerO = Offer.objects.all()
    context = {
        "offer": offerO
    }
    return render(request, 'Agence/offer.html', context)


def get_offer_c(request, id):
    offerO = Offer.objects.filter(company=id)
    context = {
        "offer": offerO,
        'id': Offer.company_id,
    }
    return render(request, 'my_offers.html', context)


def get_add_candidate(request):
    candidateC = Candidate.objects.all()
    context = {
        "candidate": candidateC
    }
    return render(request, 'Agence/add_candidate.html', context)


def get_add_company(request):
    companyC = Company.objects.all()
    context = {
        "company": companyC
    }
    return render(request, 'Agence/add_company.html', context)


def save_com(request):
    company_name = request.POST.get('company_name')
    address = request.POST.get('address')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.POST.get('creation_date') == "":
        creation_date = None
    else:
        creation_date = request.POST.get('creation_date')
    business_sector = request.POST.get('business_sector')
    headquarters = request.POST.get('headquarters')
    phone_number = request.POST.get('phone_number')
    website = request.POST.get('website')
    linkedin = request.POST.get('linkedin')
    if request.POST.get('size') == "":
        size = 0
    else:
        size = request.POST.get('size')
    # Check if the email is already used by another candidate
    if Company.objects.filter(email_address=email).exists():
        messages.error(
            request, 'This email is already registered. Please use a different email.')
        return redirect('add_company')
    # Create a new Company instance and save it to the database
    Company.objects.create(
        company_name=company_name,
        address=address,
        business_sector=business_sector,
        size=size,
        creation_date=creation_date,
        headquarters=headquarters,
        website=website,
        phone_number=phone_number,
        email_address=email,
        linkedin_url=linkedin,
        password=password,
    )
    return redirect('company')


def save_signup_com(request, email):
    company_name = request.POST.get('company_name')
    address = request.POST.get('address')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.POST.get('creation_date') == "":
        creation_date = None
    else:
        creation_date = request.POST.get('creation_date')
    business_sector = request.POST.get('business_sector')
    headquarters = request.POST.get('headquarters')
    phone_number = request.POST.get('phone_number')
    website = request.POST.get('website')
    linkedin = request.POST.get('linkedin')
    if request.POST.get('size') == "":
        size = 0
    else:
        size = request.POST.get('size')
    if Company.objects.filter(email_address=email).exists():
        messages.error(
            request, 'This email is already registered. Please use a different email.')
        return redirect('sign_com')
    # Create a new Company instance and save it to the database
    Company.objects.create(
        company_name=company_name,
        address=address,
        business_sector=business_sector,
        size=size,
        creation_date=creation_date,
        headquarters=headquarters,
        website=website,
        phone_number=phone_number,
        email_address=email,
        linkedin_url=linkedin,
        password=password,
    )
    obj = Company.objects.get(email_address=email)
    return redirect(reverse('home_com', args=[obj.pk]))


def save_signup_can(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    birth_date = request.POST.get('birth_date')
    gender = request.POST.get('gender')
    phone_number = request.POST.get('phone_number')
    email = request.POST.get('email')
    password = request.POST.get('password')
    obj = Candidate.objects.filter(email=email).first()
    if obj:
        messages.error(
            request, 'This email is already registered. Please use a different email.')
        return redirect('sign_can')
    else:
        obj=Candidate.objects.create(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            gender=gender,
            phone_number=phone_number,
            email=email,
            password=password,
        )

    # build the URL to redirect to using the candidate_id
        redirect_url = reverse('home_can', args=(obj.id_candidate,))
    # redirect the user to the URL
        return redirect(redirect_url)


def perso_info(request, id):
    obj = Candidate.objects.get(id_candidate=id)
    context = {
        "obj": obj
    }
    return render(request, 'perso_info.html', context)


def perso_info_save(request, id):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    phone_number = request.POST.get('phone_number')
    password = request.POST.get('password')
    # Create a new Candidate instance and save it to the database
    Candidate.objects.filter(pk=id).update(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        password=password,
    )
    # build the URL to redirect to using the candidate_id
    redirect_url = reverse('perso_info', args=(id,))
    # redirect the user to the URL
    return redirect(redirect_url)


def my_resume(request, id):
    obj = Candidate.objects.get(id_candidate=id)
    context = {
        "obj": obj
    }
    return render(request, 'my_resume.html', context)


def my_resume_save(request, id):
    nationality = request.POST.get('nationality')
    address = request.POST.get('address')
    city = request.POST.get('city')
    education_level = request.POST.get('education_level')
    driving_license = request.POST.get('driving_license')
    linkedin = request.POST.get('linkedin')
    technical_skills = request.POST.get('technical_skills')
    language_skills = request.POST.get('language_skills')
    social_skills = request.POST.get('social_skills')
    expertise_field = request.POST.get('expertise_field')
    # Create a new Candidate instance and save it to the database
    Candidate.objects.filter(pk=id).update(
        nationality=nationality,
        address=address,
        driving_license=driving_license,
        city=city,
        linkedin=linkedin,
        technical_skills=technical_skills,
        language_skills=language_skills,
        social_skills=social_skills,
        expertise_field=expertise_field,
        education_level=education_level,)
    # build the URL to redirect to using the candidate_id
    redirect_url = reverse('my_resume', args=(id,))
    # redirect the user to the URL
    return redirect(redirect_url)


def apply(request, id, idf):
    candidate = id
    offer = idf
    application_date = timezone.localdate()

    Postulation.objects.create(
        candidate=candidate,
        offer=offer,
        application_date=application_date,
    )
    # build the URL to redirect to using the candidate_id
    redirect_url = reverse('more_infoc', args=(id, idf,))
    # redirect the user to the URL
    return redirect(redirect_url)


def save(request):
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
    driving_license = request.POST.get('driving_license')
    linkedin = request.POST.get('linkedin')
    technical_skills = request.POST.get('technical_skills')
    language_skills = request.POST.get('language_skills')
    social_skills = request.POST.get('social_skills')
    expertise_field = request.POST.get('expertise_field')
    password = request.POST.get('password')
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
    columns = ['id_candidate', 'driving_license', 'city', 'technical_skills',
               'language_skills', 'social_skills', 'education_level', 'expertise_field']
    order_columns = ['id_candidate', 'driving_license', 'city', 'technical_skills',
                     'language_skills', 'social_skills', 'education_level', 'expertise_field']

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
                q = Q(customer_firstname__istartswith=part) | Q(
                    customer_lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs


class companyJson(BaseDatatableView):
    model = Company
    columns = ['company_id', 'address', 'headquarters', 'business_sector']
    order_columns = ['company_id', 'address',
                     'headquarters', 'business_sector']

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
                q = Q(customer_firstname__istartswith=part) | Q(
                    customer_lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs


class offerJson_c(BaseDatatableView):
    model = Offer
    columns = ['id', 'title', 'id', 'job_type', 'date_cloture', 'description',
               'skills', 'experience', 'education_level', 'number_of_positions', 'languages']
    order_columns = ['id', 'title', 'id', 'job_type', 'date_cloture', 'description',
                     'skills', 'experience', 'education_level', 'number_of_positions', 'languages']

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
                q = Q(customer_firstname__istartswith=part) | Q(
                    customer_lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs


class offerJson(BaseDatatableView):
    model = Offer
    columns = ['id', 'title', 'id', 'job_type', 'date_cloture', 'description',
               'skills', 'experience', 'education_level', 'number_of_positions', 'languages']
    order_columns = ['id', 'title', 'id', 'job_type', 'date_cloture', 'description',
                     'skills', 'experience', 'education_level', 'number_of_positions', 'languages']

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
                q = Q(customer_firstname__istartswith=part) | Q(
                    customer_lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs


class PostulationJson(BaseDatatableView):
    model = Postulation
    columns = ['id', 'candidate', 'offer', 'application_date', 'acceptation']
    order_columns = ['id', 'candidate', 'offer',
                     'application_date', 'acceptation']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def get(self, request, *args, **kwargs):
        # Override get method to return JSON response instead of HTML
        draw = int(request.GET.get('draw', 0))
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 0))
        search_value = request.GET.get('search[value]', '')

        queryset = self.filter_queryset(self.model.objects.all())
        records_total = queryset.count()

        if search_value:
            queryset = queryset.filter(
                Q(candidate_name_icontains=search_value) |
                Q(offer_name_icontains=search_value)
            )

        records_filtered = queryset.count()

        order_column_idx = int(request.GET.get('order[0][column]', 0))
        order_column = self.columns[order_column_idx]
        order_direction = request.GET.get('order[0][dir]', 'asc')
        order_by = order_column if order_direction == 'asc' else f'-{order_column}'

        queryset = queryset.order_by(order_by)
        queryset = queryset[start:start+length]

        data = [
            [
                row.candidate.id_candidate,
                row.candidate.expertise_field,
                row.offer.id,
                row.offer.field,
                f'<button onclick="acceptPostulation({row.id}, true)">Accept</button><button onclick="rejectPostulation({row.id}, false)">Reject</button>'            ]
            for row in queryset
        ]

        return JsonResponse({
            'draw': draw,
            'recordsTotal': records_total,
            'recordsFiltered': records_filtered,
            'data': data,
        })

    def update_acceptation(request, postulation_id, acceptation):
        postulation = get_object_or_404(Postulation, id=postulation_id)
        
        postulation.acceptation = acceptation
        postulation.save()
        return JsonResponse({'success': True})

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(candidate__name__istartswith=search)
                           | Q(offer__name__istartswith=search))

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