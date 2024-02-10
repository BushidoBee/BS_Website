from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .RL_DBMod import Account, Flavoring, Product, ItemOrder, RentalBook, Review

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Basic Homepage 
def homepage(request):
    context = {}
    if request.method == "GET":
        return render(request, 'RhythmandLime.htm', context)

# User Registration 


# Ordering Process 


# Rental / Order Confirmation 


# User Registration 


# User Login / Log Out 
