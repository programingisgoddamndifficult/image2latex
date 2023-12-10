from django.urls import re_path as url
from django.contrib import admin
from . import run_model
from django.urls import path

urlpatterns = [
    # url(r'^search-form$', run_model.search_form),
    # url(r'^search$', run_model.search),
    path('search_form/',run_model.search_form),
    path('search/',run_model.search)
]
