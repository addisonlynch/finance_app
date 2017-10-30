from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _


class PortfolioForm(forms.Form):
    symbol = forms.RegexField(label=_("Symbol"), max_length=5,
        regex=r'^[A-Za-z0-9]+$',
        help_text=_("Required. 5 characters or fewer. Latin letters or digits"),
        error_messages={
            'invalid': _("This value may contain only latin letters or digits"),
        })
