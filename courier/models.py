from django.db import models
from django.utils.translation import gettext_lazy as _


class Courier(models.Model):
    name = models.CharField(max_length=128, verbose_name=_("name"))

    class Meta:
        verbose_name = _("courier")
        verbose_name_plural = _("couriers")

    def __str__(self):
        return self.name
