from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

from C4D.models import RawLandRecord

class ModelSearchForm(forms.ModelForm):
    class Meta:
        model = RawLandRecord
        fields = ['legal_description', 'lot', 'block', 'tract', 'grantor', 'grantee', 'document_date', 'recording_date']

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
