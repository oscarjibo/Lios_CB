from django.http import HttpResponse
import datetime
from django.template import Template, Context
# from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render
from django.template import Context, Template, loader
from django.shortcuts import render
import datetime

def bienvenida(request):
    return HttpResponse("# bienvenido a OSIRIS")
