from django.db import models
from django.utils.translation import gettext_lazy as _
from courier.models import Courier
from django.db import models, transaction


class AbstractTransaction(models.Model):
    payment = models.PositiveIntegerField(verbose_name=_("payment"))
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name=_("date"))

    class Meta:
        abstract = True

    @transaction.atomic()
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Bonus(AbstractTransaction):
    class Meta:
        verbose_name = _("bonus")
        verbose_name_plural = _("bonuses")

    def __str__(self):
        return "{courier}-{date}".format(
            courier=self.courier.name, date=self.created_at
        )


class Penalty(AbstractTransaction):
    class Meta:
        verbose_name = _("penalty")
        verbose_name_plural = _("penalties")

    def __str__(self):
        return "{courier}-{date}".format(
            courier=self.courier.name, date=self.created_at
        )


class Trip(AbstractTransaction):
    class Meta:
        verbose_name = _("trip")
        verbose_name_plural = _("trips")

    def __str__(self):
        return "{courier}-{date}".format(
            courier=self.courier.name, date=self.created_at
        )

    @transaction.atomic()
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
