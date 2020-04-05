"""
Url definition file to redistribute incoming URL requests to django
views. Search the Django documentation for "URL dispatcher" for more
help.

"""
from django.conf.urls import url, include

# default evennia patterns
from evennia.web.urls import urlpatterns

# eventual custom patterns
custom_patterns = [
    # url(r'/desired/url/', view, name='example'),

]

custom_patterns.append( url(r'^advantages/', include('web.advantages.urls')))
custom_patterns.append( url(r'^contracts/', include('web.contracts.urls')))
custom_patterns.append( url(r'^kiths/', include('web.kiths.urls')))
custom_patterns.append( url(r'^merits/', include('web.merits.urls')))
custom_patterns.append( url(r'^powers/', include('web.powers.urls')))
custom_patterns.append( url(r'^spheres/', include('web.spheres.urls')))
custom_patterns.append( url(r'^seemings/', include('web.seemings.urls')))


# this is required by Django.
urlpatterns = custom_patterns + urlpatterns
