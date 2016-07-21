from django.conf import settings
from django.template import RequestContext, Template
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.forms.models import model_to_dict

from C4D.forms import ModelSearchForm
from C4D.models import RawLandRecord

def home(request):
    return render_to_response('home.html',{}, RequestContext(request))

def record_search(search_form):
    if not search_form.is_valid():
        raise Exception("Invalid Search Form")

    results = RawLandRecord.objects.all()
    if search_form.cleaned_data['legal_description']:
        results = results.filter(legal_description__icontains=search_form.cleaned_data['legal_description'])
    if search_form.cleaned_data['lot']:
        results = results.filter(lot__icontains=search_form.cleaned_data['lot'])
    if search_form.cleaned_data['block']:
        results = results.filter(block__icontains=search_form.cleaned_data['block'])
    if search_form.cleaned_data['tract']:
        results = results.filter(tract__icontains=search_form.cleaned_data['tract'])
    if search_form.cleaned_data['grantor']:
        results = results.filter(grantor__icontains=search_form.cleaned_data['grantor'])
    if search_form.cleaned_data['grantee']:
        results = results.filter(grantee__icontains=search_form.cleaned_data['grantee'])

    if results.count() > 1000:
        raise Exception("Search too broad.  Returned %d rows!" % results.count())
    return results

@login_required
def search(request):
    search_results = None
    if request.method == "POST":
        search_form = ModelSearchForm(request.POST)
        try:
            search_results = record_search(search_form)
        except Exception as e:
            messages.add_message(request, messages.ERROR, e)
    else:
        search_form = ModelSearchForm()

    return render_to_response('search.html',{'search_form':search_form, 'search_results':search_results}, RequestContext(request))

@login_required
def view_record(request, record_id):
    record = RawLandRecord.objects.filter(id=record_id).first()
    return render_to_response('record.html', {'record':record}, RequestContext(request))

@login_required
@permission_required('C4D.add_rawlandrecord', login_url='/')
def import_file(request):
    return render_to_response('import_file.html', {}, RequestContext(request))
