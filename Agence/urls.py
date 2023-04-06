from django import views
import os
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admine', home, name="index"),
    path('', home_a, name="home_a"),
    path('internship', internship_a , name="internship" ),
    path('job', job_a , name="job" ),
    path('more_info/<int:id>/', more_info, name='more_info'),
    path('contact', contact, name="contact"),
    path('about', about_us, name="about"),
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
    path('save_condidate', save, name="save_condidate"),
    path(r'^candidateJson$', candidateJson.as_view(), name='candidateJson'),
    path(r'^companyJson$', companyJson.as_view(), name='companyJson'),
    path(r'^offerJson$', offerJson.as_view(), name='offerJson'),
    path(r'^postulationJson$', PostulationJson.as_view(), name='postulationJson'),

]




