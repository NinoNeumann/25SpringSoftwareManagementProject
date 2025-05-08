from django.shortcuts import render,redirect,HttpResponse
from .models import *
from apscheduler.schedulers.background import BackgroundScheduler 
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job 
import datetime
from .apscheduler import initScheduler,seatInit
initScheduler()
seatInit()

# jump Page
from .log2index import topage,index,userRegister,register,distinguishIdentity