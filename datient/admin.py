from django.contrib import admin
from datient.models.doctor import Doctor
from datient.models.hospital import Hospitalization
from datient.models.infraestructure import Bed, Room
from datient.models.patient import Patient

def full_name(obj):
    return f'{obj.first_name} {obj.last_name}'

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('email', full_name, 'hierarchy')

class BedInLine(admin.TabularInline):
    model = Bed

class RoomAdmin(admin.ModelAdmin):
    inlines = [BedInLine]
    ordering = ('pk',)

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Hospitalization)
admin.site.register(Room, RoomAdmin)
admin.site.register(Patient)
