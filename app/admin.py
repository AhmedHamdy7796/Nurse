from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Patient)
admin.site.register(Nurse)
admin.site.register(Appointment)
admin.site.register(Visit)
admin.site.register(Service)
admin.site.register(Task)
admin.site.register(reservation)


