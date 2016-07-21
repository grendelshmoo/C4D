from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth.views import login, logout_then_login, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib import admin

from C4D import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search/', views.search, name='search'),
    url(r'^record/(?P<record_id>\d+)/$', views.view_record, name="view_record"),
    url(r'^import/', views.import_file, name='import_file'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login),
    url(r'^logout/$', logout_then_login),
]
