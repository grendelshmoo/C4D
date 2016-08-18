from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms.widgets import RadioSelect

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

class UploadFileForm(forms.Form):
    file = forms.FileField()

class SearchForm(forms.Form):
    legal_description = forms.CharField(max_length=100, required=False)
    leg_sel = forms.ChoiceField(widget=RadioSelect(), choices=[['leg_eq', 'Equals'], ['leg_cont', 'Contains'], ['leg_starts', 'Starts with']], label='Description Search Criteria', required=False)
    lot = forms.CharField(max_length=16, required=False)
    lot_sel = forms.ChoiceField(widget=RadioSelect(), choices=[['lot_eq', 'Equals'], ['lot_cont', 'Contains'], ['lot_starts', 'Starts with']], label='Lot Search Criteria', required=False)
    block = forms.CharField(max_length=16, required=False)
    block_sel = forms.ChoiceField(widget=RadioSelect(), choices=[['block_eq', 'Equals'], ['block_cont', 'Contains'], ['block_starts', 'Starts with']], label="Block Search Criteria", required=False)
    tract = forms.CharField(max_length=16, required=False)
    tract_sel = forms.ChoiceField(widget=RadioSelect(), choices=[['tract_eq', 'Equals'], ['tract_cont', 'Contains'], ['tract_starts', 'Starts with']], label="Tract Search Criteria", required=False)
    grantor = forms.CharField(max_length=100, label="Grantor", required=False)
    grantor_sel = forms.ChoiceField(widget=RadioSelect(), choices=[['grantor_eq', 'Equals'], ['grantor_cont', 'Contains'], ['grantor_starts', 'Starts with']], label="Grantor Search Criteria",  required=False)
    grantee = forms.CharField(max_length=100, label="Grantee", required=False)
    grantee_sel = forms.ChoiceField(widget=RadioSelect(), choices=[['grantee_eq', 'Equals'], ['grantee_cont', 'Contains'], ['grantee_starts', 'Starts with']], label="Grantee Search Criteria", required=False)
    document_date = forms.DateField(label="Document Date", required=False)
    dd_sel = forms.ChoiceField(widget=RadioSelect(), choices=[['dd_eq', 'Equals'], ['dd_less', 'Less than'], ['dd_greater', 'Greater than']], label="Document Date Criteria", required=False)
    recording_date = forms.DateField(label="Recording Date", required=False)
    rd_sel = forms.ChoiceField(widget=RadioSelect(), choices=[['rd_eq', 'Equals'], ['rd_less', 'Less than'], ['rd_greater', 'Greater than']], label="Recording Date Criteria", required=False)
    #start_date = forms.DateField(required=False)
    #end_date = forms.DateField(required=False)
