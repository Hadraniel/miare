from django.db.models.signals import post_save
from django.dispatch import receiver
from payment.models import Penalty, Bonus, Trip
from income.models import DailyIncome, WeeklyIncome
from datetime import timedelta


@receiver(post_save, sender=Trip, dispatch_uid="apply_trip_payment_on_daily_income")
def apply_trip_payment_on_daily_income(sender, instance, created, **kwargs):
    obj, created = DailyIncome.objects.update_or_create(
        courier=instance.courier, date=instance.created_at
    )
    obj.update_income()


@receiver(post_save, sender=Bonus, dispatch_uid="apply_bonus_on_daily_income")
def apply_bonus_on_daily_income(sender, instance, created, **kwargs):
    obj, created = DailyIncome.objects.update_or_create(
        courier=instance.courier, date=instance.created_at
    )
    obj.update_income()


@receiver(post_save, sender=Penalty, dispatch_uid="apply_penalty_on_daily_income")
def apply_penalty_on_daily_income(sender, instance, created, **kwargs):
    obj, created = DailyIncome.objects.update_or_create(
        courier=instance.courier, date=instance.created_at
    )
    obj.update_income()


@receiver(
    post_save, sender=DailyIncome, dispatch_uid="apply_daily_income_on_weekly_income"
)
def apply_daily_income_on_weekly_income(sender, instance, created, **kwargs):
    date = instance.date
    week_start = date - timedelta(days=(date.weekday() + 2) % 7)
    obj, created = WeeklyIncome.objects.update_or_create(
        courier=instance.courier, week_start=week_start
    )
    obj.update_income()
