from django.contrib import admin
from django.forms import TextInput, Textarea

from django.db import models

from webplot.models import plot1d

class plot1dAdmin(admin.ModelAdmin):
    pass

admin.site.register(plot1d, plot1dAdmin)
