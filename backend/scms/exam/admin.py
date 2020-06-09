from django.contrib import admin
from .models import Exam, Questionset, Scorecard

admin.site.register(Exam)
admin.site.register(Questionset)
admin.site.register(Scorecard)
