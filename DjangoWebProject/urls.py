"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

'''
                    <li><a href="{% url 'home' %}">Home</a></li>
                    <li><a href="{% url 'asteroid_data' %}">Asteroid Data</a></li>
                    <li><a href="{% url 'nasa_arm' %}">Nasa ARM</a></li>
                    <li><a href="{% url 'educate' %}">Educate</a></li>
                    <li><a href="{% url 'knapsack' %}">Mining</a></li>
'''

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^asteroid_data$', 'app.views.asteroid_data', name='asteroid_data'),
    url(r'^nasa_arm$', 'app.views.nasa_arm', name='nasa_arm'),
    url(r'^educate$', 'app.views.educate', name='educate'),
    url(r'^knapsack$', 'app.views.knapsack', name='knapsack'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
