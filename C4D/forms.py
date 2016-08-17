from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

from C4D.models import RawLandRecord

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('auto_id', '%s')
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                'placeholder' : field.help_text
                })

class ModelSearchForm(forms.ModelForm):
    class Meta:
        model = RawLandRecord
        fields = ['legal_description', 'lot', 'block', 'tract', 'grantor', 'grantee', 'document_date', 'recording_date']
        help_texts = {
            'document_date' : 'e.g. 1998-01-01',
            'recording_date' : 'e.g. 1998-01-01'
        }

class UploadFileForm(forms.Form):
    file = forms.FileField()

class SearchForm(forms.Form):
    lot = forms.CharField(max_length=16, required=False)
    block = forms.CharField(max_length=16, required=False)
    tract = forms.CharField(max_length=16, required=False)
    grantor = forms.CharField(max_length=100, label="Grantor", required=False)
    grantee = forms.CharField(max_length=100, label="Grantee", required=False)
    document_date = forms.DateField(label="Document Date", required=False)
    recording_date = forms.DateField(label="Recording Date", required=False)
    #start_date = forms.DateField(required=False)
    #end_date = forms.DateField(required=False)
