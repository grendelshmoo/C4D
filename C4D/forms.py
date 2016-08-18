from django import forms
from django.utils import timezone
from django.forms.widgets import RadioSelect
from django.utils.safestring import mark_safe

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class UploadFileForm(forms.Form):
    file = forms.FileField()

class SearchForm(forms.Form):
    island = forms.CharField(max_length=100, required=False)
    legal_description = forms.CharField(max_length=100, required=False)
    lot = forms.CharField(max_length=16, required=False)
    lot_sel = forms.ChoiceField(widget=RadioSelect(renderer=HorizontalRadioRenderer), choices=[['lot_eq', 'Equals'], ['lot_cont', 'Contains'], ['lot_starts', 'Starts with']], label='Lot Search Criteria', required=False)
    block = forms.CharField(max_length=16, required=False)
    block_sel = forms.ChoiceField(widget=RadioSelect(renderer=HorizontalRadioRenderer), choices=[['block_eq', 'Equals'], ['block_cont', 'Contains'], ['block_starts', 'Starts with']], label="Block Search Criteria", required=False)
    tract = forms.CharField(max_length=16, required=False)
    tract_sel = forms.ChoiceField(widget=RadioSelect(renderer=HorizontalRadioRenderer), choices=[['tract_eq', 'Equals'], ['tract_cont', 'Contains'], ['tract_starts', 'Starts with']], label="Tract Search Criteria", required=False)
    grantor = forms.CharField(max_length=100, label="Grantor", required=False)
    grantor_sel = forms.ChoiceField(widget=RadioSelect(renderer=HorizontalRadioRenderer), choices=[['grantor_eq', 'Equals'], ['grantor_cont', 'Contains'], ['grantor_starts', 'Starts with']], label="Grantor Search Criteria",  required=False)
    grantee = forms.CharField(max_length=100, label="Grantee", required=False)
    grantee_sel = forms.ChoiceField(widget=RadioSelect(renderer=HorizontalRadioRenderer), choices=[['grantee_eq', 'Equals'], ['grantee_cont', 'Contains'], ['grantee_starts', 'Starts with']], label="Grantee Search Criteria", required=False)
    document_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'e.g. 1990-01-01'}), label="Document Date", required=False)
    document_date_range = forms.DateField(widget=forms.TextInput(attrs={'class': 'dd-hidden', 'placeholder':'e.g. 1998-01-01'}), required=False, label='To')
    dd_sel = forms.ChoiceField(widget=RadioSelect(renderer=HorizontalRadioRenderer, attrs={'onclick': 'ddRange()'}), choices=[['dd_range', 'Range'], ['dd_eq', 'Equals'], ['dd_less', 'Less than'], ['dd_greater', 'Greater than']], label="Document Date Criteria", required=False)
    recording_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'e.g. 1990-01-01'}), label="Recording Date", required=False)
    recording_date_range = forms.DateField(widget=forms.TextInput(attrs={'class': 'rd-hidden', 'placeholder': 'e.g. 1998-01-01'}), label="To", required=False)
    rd_sel = forms.ChoiceField(widget=RadioSelect(renderer=HorizontalRadioRenderer, attrs={'onclick': 'rdRange()'}), choices=[['rd_range', 'Range'], ['rd_eq', 'Equals'], ['rd_less', 'Less than'], ['rd_greater', 'Greater than']], label="Recording Date Criteria", required=False)
    #start_date = forms.DateField(required=False)
    #end_date = forms.DateField(required=False)
