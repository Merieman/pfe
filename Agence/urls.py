from django import views
import os
from django.urls import path, include
from .views import *
import Agence.views as view
urlpatterns = [
    path('update_acceptation/<int:postulation_id>/<str:acceptation>/',view.PostulationJson.update_acceptation,name='update_acceptation'),
    path('admine', home, name="index"),
    path('', home_a, name="home_a"),
    path('home_com/<int:obj_id>/', home_com, name="home_com"),
    path('home_can/<int:obj_id>/', home_can, name="home_can"),
    path('internship', internship_a , name="internship" ),
    path('job', job_a , name="job" ),
    path('job_can/<int:id>/', job_can, name="job_can"),
    path('apply/<int:id>/<str:idf>/', apply, name='apply'),
    path('app_job/<int:id>/', app_job , name="app_job"),
    path('app_int/<int:id>/', app_int , name="app_int"),
    path('list_can/<int:id>/', list_cand, name="list_can"),
    path('internship_can/<int:id>/', internship_can, name="internship_can"),
    path('more_info/<int:id>/', more_info, name='more_info'),
    path('more_infoc/<int:id>/<int:idf>/', more_infoc, name='more_infoc'),
    path('contact', contact, name="contact"),    
    path('contact_can/<int:id>/', contact_can, name="contact_can"),    
    path('contact_com', contact_com, name="contact_com"),    
    path('about', about_us, name="about"),
    path('about_can/<int:id>/', about_us_can, name="about_can"),    
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
    path('my_offers/<int:id>/', get_offer_c, name="my_offers"),
    path('postulation', get_postulation, name="postulation"),
    path('add_candidate', get_add_candidate, name="add_candidate"),
    path('add_company', get_add_company, name="add_company"),
    path('save_condidate', save, name="save_condidate"),
    path('save_company', save_com, name="save_company"),
    path('save_signup_can', save_signup_can, name="save_signup_can"),
    path('save_login_can', save_login_can, name="save_login_can"),
    path('save_login_com', save_login_com, name="save_login_com"),

    path('perso_info/<int:id>/', perso_info , name= "perso_info"),
    path('perso_info_save/<int:id>/', perso_info_save , name= "perso_info_save"),
    path('my_resume/<int:id>/', my_resume , name= "my_resume"),
    path('my_resume_save/<int:id>/', my_resume_save , name= "my_resume_save"),
    path('save_signup_com/<str:email>/', save_signup_com, name="save_signup_com"),
    path(r'^candidateJson$', candidateJson.as_view(), name='candidateJson'),
    path(r'^companyJson$', companyJson.as_view(), name='companyJson'),
    path(r'^offerJson$', offerJson.as_view(), name='offerJson'),
    path(r'^offerJson_c$', offerJson_c.as_view(), name='offerJson_c'),
    path(r'^postulationJson$', PostulationJson.as_view(), name='postulationJson'),

]




