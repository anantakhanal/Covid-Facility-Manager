from django.contrib import admin
from .models import *
# Register your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Hospital)
def afterHospitalSave(signal, instance, **kwargs):
    facilites= Facility.objects.all()
    for facility in facilites:
       availibility = Availability(hospital = instance, facility= facility)
       availibility.save()

@receiver(post_save, sender = Facility)
def afterFacilitySave(signal, instance, **kwargs):
    hospitals = Hospital.objects.all()
    for hospital in hospitals:
        availibility = Availability(hospital = hospital, facility= instance)
        availibility.save()




class FacilityAdmin(admin.ModelAdmin):
    model = Facility
    list_display = ['title',]



class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name', 'state']


class HospitalAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name', 'phone', 'address', 'city']

class AvailabilityAdmin(admin.ModelAdmin):
    model = Availability
    list_display = [ 'hospital','facility', 'updated_at' ,'available', 'total']
    list_editable = ['available', 'total']

admin.site.register(State)
admin.site.register(City, CityAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Availability,AvailabilityAdmin)
