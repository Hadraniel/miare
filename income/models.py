from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.db.models import Sum
from datetime import timedelta
from courier.models import Courier
from payment.models import Trip, Bonus, Penalty


class DailyIncome(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.PROTECT)
    date = models.DateField(verbose_name=_("date"))
    total_income = models.IntegerField(default=0)

    class Meta:
        unique_together = ("courier", "date")
        verbose_name = _("daily income")
        verbose_name_plural = _("daily incomes")

    def __str__(self):
        return "{courier}-{date}".format(courier=self.courier.name, date=self.date)

    def update_income(self):
        trip_income = Trip.objects.filter(
            courier=self.courier, created_at=self.date
        ).aggregate(total_income=Sum("payment"))["total_income"]
        bonus_income = Bonus.objects.filter(
            courier=self.courier, created_at=self.date
        ).aggregate(total_income=Sum("payment"))["total_income"]
        penalty_income = Penalty.objects.filter(
            courier=self.courier, created_at=self.date
        ).aggregate(total_income=Sum("payment"))["total_income"]
        self.total_income = (
            (trip_income or 0) + (bonus_income or 0) - (penalty_income or 0)
        )
        self.save()


class WeeklyIncome(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.PROTECT)
    week_start = models.DateField(verbose_name=_("week start"))
    total_income = models.IntegerField(default=0, verbose_name=_("total income"))

    class Meta:
        unique_together = ("courier", "week_start")
        verbose_name = _("weekly income")
        verbose_name_plural = _("weekly incomes")

    def __str__(self):
        return "{courier}-{week}".format(
            courier=self.courier.name, week=self.week_start
        )

    def clean(self):
        if self.week_start.weekday() != 5:
            raise ValidationError(_("Week Start should be saturday only!"))

    def update_income(self):
        self.total_income = DailyIncome.objects.filter(
            date__gte=self.week_start, date__lt=self.week_start + timedelta(days=7)
        ).aggregate(total_weekly_income=Sum("total_income"))["total_weekly_income"]
        self.save()
