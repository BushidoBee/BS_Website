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


# Login / Log Out View
def login_logout(request):
    context = {}
    if request.method == "POST":
        user = request.POST['username']
        password = request.POST['psw']
        logon_user = authenticate(username=user, password=password)
        if logon_user is not None:
            login(request, logon_user)
            return redirect('Homepage')
        else:
            context['message'] = "Invalid username or password, please try again."
            return render(request, 'Templates\login.htm', context)
    else:
        return render(request, 'djangoapp/index.html', context)


# User Registration 
def known_regUser(request):
    # Add code here
    details = {}
    details["warn_msg"] = "User is already registered, please login with known credentials"
    
    return render(request, 'login.htm', details)


def registerUser(request):
    # Add code here
    details = {}

    return redirect(request, 'Registration.htm', details) # Template not created yet





# Ordering Process 
def FUNCTNAME(request):
    # Add code here
    details = {}

    
    return redirect(request, 'RL_Booking.htm.htm', details) # Template not created yet



# Rental / Order Confirmation 
def FUNCTNAME(request):
    # Add code here
    details = {}

    
    return redirect(request, '???.htm', details) # Template not created yet



# User Registration 
def FUNCTNAME(request):
    # Add code here
    details = {}

    
    return redirect(request, '???.htm', details) # Template not created yet
