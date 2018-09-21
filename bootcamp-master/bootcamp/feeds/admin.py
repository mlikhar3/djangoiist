from django.contrib import admin
from django import forms
from . import models

# Register your models here.
from .models import *

admin.site.register(Feed)