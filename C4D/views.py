from django.conf import settings
from django.template import RequestContext, Template
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.forms.models import model_to_dict

import xlrd

from C4D.forms import ModelSearchForm, UploadFileForm
from C4D.models import RawLandRecord, ImportLog
from C4D.importer import Importer

def home(request):
    return render_to_response('home.html',{}, RequestContext(request))

@login_required
def search(request):
    search_results = None
    if request.method == "POST":
        search_form = ModelSearchForm(request.POST)
        if not search_form.is_valid():
            messages.add_message(request, messages.ERROR, "Invalid Search Form")
        else:
            search_results = RawLandRecord.objects.all()
            if search_form.cleaned_data['legal_description']:
                search_results = search_results.filter(legal_description__icontains=search_form.cleaned_data['legal_description'])
            if search_form.cleaned_data['lot']:
                search_results = search_results.filter(lot__icontains=search_form.cleaned_data['lot'])
            if search_form.cleaned_data['block']:
                search_results = search_results.filter(block__icontains=search_form.cleaned_data['block'])
            if search_form.cleaned_data['tract']:
                search_results = search_results.filter(tract__icontains=search_form.cleaned_data['tract'])
            if search_form.cleaned_data['grantor']:
                search_results = search_results.filter(grantor__icontains=search_form.cleaned_data['grantor'])
            if search_form.cleaned_data['grantee']:
                search_results = search_results.filter(grantee__icontains=search_form.cleaned_data['grantee'])
            if search_results.count() > 1000:
                messages.add_message(request, messages.ERROR, "Search too broad.  Returned %d rows!" % search_results.count())
                search_result = None
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
    logs = None
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload_file = request.FILES['file']
            xls_book = xlrd.open_workbook(file_contents=upload_file.read())
            importer = Importer(request.user, upload_file.name, print_to_console=False)
            importer.import_data(xls_book)
            logs = importer.logs
    else:
        form = UploadFileForm()
    import_logs = ImportLog.objects.all()[:5]
    return render_to_response('import_file.html', {'form':form, 'logs': logs, 'import_logs': import_logs}, RequestContext(request))
