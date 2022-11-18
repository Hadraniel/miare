from django.contrib import admin

from .models import DailyIncome, WeeklyIncome

admin.site.register(DailyIncome)
admin.site.register(WeeklyIncome)
