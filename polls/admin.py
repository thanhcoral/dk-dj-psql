from django.contrib import admin

from polls.models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('visit_date', 'full_name', 'phone', 'address')
admin.site.register(Patient, PatientAdmin)