from django.contrib import admin

from .models import Education, Experience, Skill, Interest, Award


admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Interest)
admin.site.register(Award)
