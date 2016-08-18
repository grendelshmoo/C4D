from django.conf import settings
from django.template import RequestContext, Template
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.forms.models import model_to_dict
from django.utils import timezone
from django.core.urlresolvers import reverse

from C4D.forms import SearchForm, UploadFileForm
from C4D.models import RawLandRecord, ImportLog
from C4D.importer import Importer

import xlrd

def home(request):
    rec_count = RawLandRecord.objects.all().count()
    islands_query = RawLandRecord.objects.values('island').distinct()
    islands = {}
    for row in islands_query:
        i = row['island']
        c = RawLandRecord.objects.filter(island=i).count()
        if not i:
            i = 'Unknown'
        islands[i] = c
    return render_to_response('home.html',{'rec_count':rec_count, 'islands': islands}, RequestContext(request))

@login_required
def search(request):
    query = []
    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if not search_form.is_valid():
            messages.add_message(request, messages.ERROR, "Invalid Search Form")
        else:
            if search_form.cleaned_data['island']:
                query.append('island__icontains=' + str(search_form.cleaned_data['island']))
            if search_form.cleaned_data['legal_description']:
                data = str(search_form.cleaned_data['legal_description'])
                query.append('legal_description__icontains=' + data)
            if search_form.cleaned_data['lot']:
                lot = str(search_form.cleaned_data['lot'])
                if search_form.cleaned_data['lot_sel']:
                    if request.POST.get('lot_sel') == 'lot_eq':
                        query.append('lot=' + lot)
                    elif request.POST.get('lot_sel') == 'lot_cont':
                        query.append('lot__icontains=' + lot)
                    elif request.POST.get('lot_sel') == 'lot_starts':
                        query.append('lot__startswith' + lot)
                else:
                    query.append('lot__icontains=' + lot)
            if search_form.cleaned_data['block']:
                block = str(search_form.cleaned_data['block'])
                if search_form.cleaned_data['block_sel']:
                    if request.POST.get('block_sel') == 'block_eq':
                        query.append('block=' + block)
                    elif request.POST.get('block_sel') == 'block_cont':
                        query.append('block__icontains=' + block)
                    elif request.POST.get('block_sel') == 'block_starts':
                        query.append('block__startswith=' + block)
                else:
                    query.append('block__icontains=' + block)
            if search_form.cleaned_data['tract']:
                tract = str(search_form.cleaned_data['tract'])
                if search_form.cleaned_data['tract_sel']:
                    if request.POST.get('tract_sel' == 'tract_eq'):
                        query.append('tract=' + tract)
                    elif request.POST.get('tract_sel' == 'tract_cont'):
                        query.append('tract__icontains=' + tract)
                    elif request.POST.get('tract_sel' == 'tract_starts'):
                        query.append('tract__startswith=' + tract)
                else:
                    query.append('tract__icontains=' + tract)
            if search_form.cleaned_data['grantor']:
                grantor = str(search_form.cleaned_data['grantor'])
                if search_form.cleaned_data['grantor_sel']:
                    if request.POST.get('grantor_sel') == 'grantor_eq':
                        query.append('grantor=' + grantor)
                    elif request.POST.get('grantor_sel') == 'grantor_cont':
                        query.append('grantor__icontains=' + grantor)
                    elif request.POST.get('grantor_sel') == 'grantor_starts':
                        query.append('grantor__startswith=' + grantor)
                else:
                    query.append('grantor__icontains=' + grantor)
            if search_form.cleaned_data['grantee']:
                grantee = str(search_form.cleaned_data['grantee'])
                if search_form.cleaned_data['grantee_sel']:
                    if request.POST.get('grantee_sel') == 'grantee_eq':
                        query.append('grantee=' + grantee)
                    elif request.POST.get('grantee_sel') == 'grantee_cont':
                        query.append('grantee__icontains=' + grantee)
                    elif request.POST.get('grantee_sel') == 'grantee_starts':
                        query.append('grantee__startswith=' + grantee)
                else:
                    query.append('grantee__icontains=' + grantee)
            if search_form.cleaned_data['document_date']:
                dd = str(search_form.cleaned_data['document_date'])
                if search_form.cleaned_data['dd_sel']:
                    if request.POST.get('dd_sel') == 'dd_range':
                        if search_form.cleaned_data['document_date_range']:
                            lte_range = str(search_form.cleaned_data['document_date_range'])
                            query.append('document_date__gte=' + dd + '&document_date__lte=' + lte_range)
                        else:
                            query.append('document_date__gte=' + dd)
                    elif request.POST.get('dd_sel') == 'dd_eq':
                        query.append('document_date=' + dd)
                    elif request.POST.get('dd_sel') == 'dd_less':
                        query.append('document_date__lte=' + dd)
                    elif request.POST.get('dd_sel') == 'dd_greater':
                        query.append('document_date__gte=' + dd)
                else:
                    query.append('document_date=' + dd)
            if search_form.cleaned_data['recording_date']:
                rd = str(search_form.cleaned_data['recording_date'])
                if search_form.cleaned_data['rd_sel']:
                    if request.POST.get('rd_sel') == 'rd_range':
                        if search_form.cleaned_data['recording_date_range']:
                            lte_range = str(search_form.cleaned_data['recording_date_range'])
                            query.append('recording_date__gte=' + rd + '&recording_date__lte=' + lte_range)
                        else:
                            query.append('document_date__gte=' + dd)
                    elif request.POST.get('rd_sel') == 'rd_eq':
                        query.append('recording_date=' + rd)
                    elif request.POST.get('rd_sel') == 'rd_less':
                        query.append('recording_date__lte=' + rd)
                    elif request.POST.get('rd_sel') == 'rd_greater':
                        query.append('recording_date__gte=' + rd)
                else:
                    query.append('recording_date=' + rd)
            query_string = '&'.join(query)
            url = '?' + query_string
            return HttpResponseRedirect(reverse('admin:C4D_rawlandrecord_changelist') + url)
    else:
        search_form = SearchForm()
    return render_to_response('search.html',{'search_form':search_form}, RequestContext(request))

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
        if 'log_id' in request.POST:
            id = request.POST['log_id']
            log = ImportLog.objects.get(pk=id).delete()
            messages.success(request, 'Import deleted')
        elif form.is_valid():
            upload_file = request.FILES['file']
            xls_book = xlrd.open_workbook(file_contents=upload_file.read())
            importer = Importer(request.user, upload_file.name)
            importer.import_data(xls_book)
            logs = importer.messages
    else:
        form = UploadFileForm()
    import_logs = ImportLog.objects.all().order_by('-start_ts')[:20]
    for log in import_logs:
        e = log.end_ts

        if not e:
            e = timezone.now()
        time_diff = e.replace(microsecond = 0) - log.start_ts.replace(microsecond = 0)
        log.duration = str(time_diff)

        if log.duration == '0:00:00':
            log.duration = 'less than a second'
    return render_to_response('import_file.html', {'form':form, 'logs': logs, 'import_logs': import_logs}, RequestContext(request))
