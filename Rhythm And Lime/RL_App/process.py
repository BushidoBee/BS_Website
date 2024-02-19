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
def known_regUser(request):
    # Add code here
    details = {}
    details["warn_msg"] = "User is already register, please login with known credentials"
    
        return render(request, 'login.htm', details)
        
def registerUser(request):
    # Add code here
    details = {}

    
        return redirect(request, 'Registration.htm', details) # Template not created yet

# Login / Log Out View
def FUNCTNAME(request):
    # Add code here
    
        return render(request, 'login.htm', details)

# Ordering Process 
def FUNCTNAME(request):
    # Add code here
    details = {}

    
        return redirect(request, 'Orderpage.htm', details) # Template not created yet


# Rental / Order Confirmation 
def FUNCTNAME(request):
    # Add code here
    details = {}

    
        return redirect(request, '???.htm', details)


# User Registration 
def FUNCTNAME(request):
    # Add code here
    details = {}

    
        return redirect(request, '???.htm', details)
