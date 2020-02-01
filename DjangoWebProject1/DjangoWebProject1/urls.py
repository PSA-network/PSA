"""
Definition of urls for DjangoWebProject1.
"""#(3)импорт функций для настройки доступа к загруженным файлам

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.conf.urls.static import static                                                                    
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^links$', app.views.links, name='links'),
    url(r'^blog$', app.views.blog, name='blog'), 
    url(r'^news$', app.views.news, name='news'),
    url(r'^news/(?P<parametr>\d+)$', app.views.newspost, name='newspost'),
    url(r'^newpost$', app.views.newpost, name='newpost'),
    url(r'^services$', app.views.services, name='services'),
    url(r'^(?P<parametr>\d+)/$', app.views.blogpost, name='blogpost'),
    url(r'^orders$', app.views.orders, name='orders'),
    url(r'^registration$', app.views.registration, name='registration'),
    url(r'^login/$',

    
    
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Вход',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration$', app.views.registration, name='registration'), # для регистрации
   #регистрируем статические данные
]
urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()