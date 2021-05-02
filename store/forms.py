from django.forms import EmailInput, ModelForm, TextInput
from django.forms.utils import ErrorList

from .models import Contact


class ParagraphErrorList(ErrorList):

    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div>%s</div>' % ''.join(['<p class="text-danger">%s</p>' % e for e in self])


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email']
        widget = {
            'name': TextInput(attrs={'class': 'form-control form-control-sm'}),
            'email': EmailInput(attrs={'class': 'form-control form-control-sm'})
        }
