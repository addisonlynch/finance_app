from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User


class Stock(models.Model):
    user = models.ForeignKey(User)
    symbol = models.CharField(_('Symbol'), max_length=5)


