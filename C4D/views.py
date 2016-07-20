from django.conf import settings
from django.template import RequestContext, Template
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

def home(request):
    return render_to_response('home.html',{'has_permission':True}, RequestContext(request))

@login_required
def search(request):
    return render_to_response('search.html',{'has_permission':True}, RequestContext(request))

@login_required
@permission_required('C4D.add_rawlandrecord', login_url='/')
def import_file(request):
    return render_to_response('import_file.html',{'has_permission':True}, RequestContext(request))
