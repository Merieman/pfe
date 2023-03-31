from django import views
import os
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name="index"),
    path('candidate', get_candidate, name="candidate"),
    path('company', get_company, name="company"),
    path('offer', get_offer, name="offer"),
    path('add_candidate', get_add_candidate, name="add_candidate"),
    path(r'^candidateJson$', candidateJson.as_view(), name='candidateJson'),
    path(r'^companyJson$', companyJson.as_view(), name='companyJson'),
    path(r'^offerJson$', offerJson.as_view(), name='offerJson'),

]



