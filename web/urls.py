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

custom_patterns.append( url(r'^advantages/', include('codes.web.advantages.urls')))
custom_patterns.append( url(r'^auspices/', include('codes.web.auspices.urls')))
custom_patterns.append( url(r'^clans/', include('codes.web.clans.urls')))
custom_patterns.append( url(r'^coils/', include('codes.web.coils.urls')))
custom_patterns.append( url(r'^contracts/', include('codes.web.contracts.urls')))
custom_patterns.append( url(r'^covenants/', include('codes.web.covenants.urls')))
custom_patterns.append( url(r'^cruac/', include('codes.web.cruac.urls')))
custom_patterns.append( url(r'^devotions/', include('codes.web.devotions.urls')))
custom_patterns.append( url(r'^disciplines/', include('codes.web.disciplines.urls')))
custom_patterns.append( url(r'^gifts/', include('codes.web.gifts.urls')))
custom_patterns.append( url(r'^kiths/', include('codes.web.kiths.urls')))
custom_patterns.append( url(r'^lodges/', include('codes.web.lodges.urls')))
custom_patterns.append( url(r'^merits/', include('codes.web.merits.urls')))
custom_patterns.append( url(r'^paths/', include('codes.web.paths.urls')))
custom_patterns.append( url(r'^powers/', include('codes.web.powers.urls')))
custom_patterns.append( url(r'^rites/', include('codes.web.rites.urls')))
custom_patterns.append( url(r'^scales/', include('codes.web.scales.urls')))
custom_patterns.append( url(r'^seemings/', include('codes.web.seemings.urls')))
custom_patterns.append( url(r'^spheres/', include('codes.web.spheres.urls')))
custom_patterns.append( url(r'^theban/', include('codes.web.theban.urls')))
custom_patterns.append( url(r'^tribes/', include('codes.web.tribes.urls')))


# this is required by Django.
urlpatterns = custom_patterns + urlpatterns
