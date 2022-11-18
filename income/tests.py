from django.test import TestCase
import datetime
from courier.models import Courier
from payment.models import Trip, Bonus, Penalty
from income.models import DailyIncome


class TestAppModels(TestCase):
    def setUp(self):
        pass

    def test_model_str(self):
        courier = Courier.objects.create(name="Ali")
        date = datetime.date.today()
        daily = DailyIncome.objects.create(courier=courier, date=date)
        self.assertEqual(
            str(daily),
            "{courier}-{date}".format(courier=courier.name, date=date),
        )

    def test_method_update_income(self):
        courier = Courier.objects.create(name="Ali")
        date = datetime.date.today()
        trip = Trip.objects.create(courier=courier, created_at=date, payment=100)
        bonus = Bonus.objects.create(courier=courier, created_at=date, payment=200)
        penalty = Penalty.objects.create(courier=courier, created_at=date, payment=50)
        daily = DailyIncome.objects.get(courier=courier, date=date)
        payment = trip.payment + bonus.payment - penalty.payment
        self.assertEqual(daily.total_income, payment)

    def test_method_update_income_trip_only(self):
        courier = Courier.objects.create(name="Ali")
        date = datetime.date.today()
        trip = Trip.objects.create(courier=courier, created_at=date, payment=100)
        daily = DailyIncome.objects.get(courier=courier, date=date)
        payment = trip.payment
        self.assertEqual(daily.total_income, payment)

    def test_method_update_income_bonus_only(self):
        courier = Courier.objects.create(name="Ali")
        date = datetime.date.today()
        bonus = Bonus.objects.create(courier=courier, created_at=date, payment=200)
        daily = DailyIncome.objects.get(courier=courier, date=date)
        payment = bonus.payment
        self.assertEqual(daily.total_income, payment)

    def test_method_update_income_penalty_only(self):
        courier = Courier.objects.create(name="Ali")
        date = datetime.date.today()
        penalty = Penalty.objects.create(courier=courier, created_at=date, payment=50)
        daily = DailyIncome.objects.get(courier=courier, date=date)
        payment = 0 - penalty.payment
        self.assertEqual(daily.total_income, payment)

    def test_method_update_income_bonus_penalty_only(self):
        courier = Courier.objects.create(name="Ali")
        date = datetime.date.today()
        bonus = Bonus.objects.create(courier=courier, created_at=date, payment=200)
        penalty = Penalty.objects.create(courier=courier, created_at=date, payment=50)
        daily = DailyIncome.objects.get(courier=courier, date=date)
        payment = bonus.payment - penalty.payment
        self.assertEqual(daily.total_income, payment)

    def test_method_update_income_trip_penalty_only(self):
        courier = Courier.objects.create(name="Ali")
        date = datetime.date.today()
        trip = Trip.objects.create(courier=courier, created_at=date, payment=100)
        penalty = Penalty.objects.create(courier=courier, created_at=date, payment=50)
        daily = DailyIncome.objects.get(courier=courier, date=date)
        payment = trip.payment - penalty.payment
        self.assertEqual(daily.total_income, payment)
