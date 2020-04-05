# URL patterns for the character app

from django.conf.urls import url
from web.kiths.views import sheet 
from web.kiths.views import editor
from web.kiths.views import editted
from web.kiths.views import create
from web.kiths.views import created
from web.kiths.views import list


urlpatterns = [
    url(r'^view/(?P<object_id>([a-zA-Z0-9%\s\'-])+)/$', sheet, name="sheet"),
    url(r'^edit/(?P<object_id>([a-zA-Z0-9%\s\'-])+)/$', editor, name="editor"),
    url(r'^editted/$', editted, name="editted"),
    url(r'^create/$', create, name="create"),
    url(r'^created/$', created, name="created"),
    url(r'^list/$', list, name="list")
]