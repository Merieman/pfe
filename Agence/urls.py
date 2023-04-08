from django import views
import os
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admine', home, name="index"),
    path('', home_a, name="home_a"),
    path('home_com/<int:obj_id>/', home_com, name="home_com"),
    path('home_can', home_can, name="home_can"),
    path('internship', internship_a , name="internship" ),
    path('job', job_a , name="job" ),
    path('job_can', job_can, name="job_can"),
    path('internship_can', internship_can, name="internship_can"),
    path('more_info/<int:id>/', more_info, name='more_info'),
    path('more_infoc/<int:id>/', more_infoc, name='more_infoc'),
    path('contact', contact, name="contact"),    
    path('contact_can', contact_can, name="contact_can"),    
    path('contact_com', contact_com, name="contact_com"),    
    path('about', about_us, name="about"),
    path('about_can', about_us_can, name="about_can"),    
    path('about_com', about_us_com, name="about_com"),    
    path('CorC_L', L_c_c, name="chooseL"),
    path('CorC_S', S_c_c, name="chooseS"),
    path('signup_can', sign_can, name="sign_can"),
    path('signup_com', sign_com, name="sign_com"),
    path('login_com', log_com, name="log_com"),
    path('login_can' , log_can , name="log_can"),
    path('candidate', get_candidate, name="candidate"),
    path('company', get_company, name="company"),
    path('offer', get_offer, name="offer"),
    path('postulation', get_postulation, name="postulation"),
    path('add_candidate', get_add_candidate, name="add_candidate"),
    path('add_company', get_add_company, name="add_company"),
    path('save_condidate', save, name="save_condidate"),
    path('save_company', save_com, name="save_company"),
    path('save_signup_can', save_signup_can, name="save_signup_can"),
    path('save_signup_com/<str:email>/', save_signup_com, name="save_signup_com"),
    path(r'^candidateJson$', candidateJson.as_view(), name='candidateJson'),
    path(r'^companyJson$', companyJson.as_view(), name='companyJson'),
    path(r'^offerJson$', offerJson.as_view(), name='offerJson'),
    path(r'^postulationJson$', PostulationJson.as_view(), name='postulationJson'),

]




