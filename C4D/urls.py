from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth.views import login, logout_then_login, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib import admin

from C4D import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^import/', views.import_file, name='import_file'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login),
    url(r'^logout/$', logout_then_login),
    #url(r'^reset/$', views.password_reset, {'template_name': 'password_reset_form.html', 'email_template_name': 'email/password_reset_email.txt'}, 'password_reset'),
    #url(r'^reset/done/$', password_reset_done, {'template_name': 'password_reset_done.html'}, 'password_reset_done'),
    #url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'password_reset_confirm.html'}, 'password_reset_confirm'),
    #url(r'^reset/complete/$', password_reset_complete, {'template_name': 'password_reset_complete.html'}, 'password_reset_complete'),

]

admin.site.site_header = settings.SITE_TITLE
