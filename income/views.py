from django.shortcuts import render

from rest_framework import generics
from .models import WeeklyIncome
from .serializers import WeeklyIncomeSerializer
from django.utils.dateparse import parse_date
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _


class WeeklyIncomeListView(generics.ListAPIView):
    queryset = WeeklyIncome.objects.all()
    serializer_class = WeeklyIncomeSerializer

    def filter_queryset(self, queryset):
        if (
            "from_date" in self.request.query_params
            and "to_date" in self.request.query_params
        ):
            try:
                from_date = parse_date(self.request.query_params["from_date"])
                to_date = parse_date(self.request.query_params["to_date"])
                if from_date is None or to_date is None:
                    raise exceptions.ValidationError(
                        _("Dates should be well formatted!")
                    )
                queryset = queryset.objects.filter(
                    week_start__gte=from_date,
                    week_start__lte=to_date,
                )
            except ValueError:
                raise exceptions.ValidationError(_("Dates should be valid!"))

        return queryset
