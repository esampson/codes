# URL patterns for the character app

from django.conf.urls import url
from web.advantages.views import sheet 
from web.advantages.views import editor
from web.advantages.views import editted
from web.advantages.views import create
from web.advantages.views import created
from web.advantages.views import list


urlpatterns = [
    url(r'^view/(?P<object_id>([a-zA-Z0-9%\s\'-])+)/$', sheet, name="sheet"),
    url(r'^edit/(?P<object_id>([a-zA-Z0-9%\s\'-])+)/$', editor, name="editor"),
    url(r'^editted/$', editted, name="editted"),
    url(r'^create/$', create, name="create"),
    url(r'^created/$', created, name="created"),
    url(r'^list/$', list, name="list")
]