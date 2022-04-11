from django.contrib import admin

# Register your models here.
from statistiky.models import Person, Temperature, Heart_rate, Sleep, Statistic
admin.site.register(Person)
admin.site.register(Temperature)
admin.site.register(Heart_rate)
admin.site.register(Sleep)
admin.site.register(Statistic)