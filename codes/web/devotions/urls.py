# URL patterns for the character app

from django.conf.urls import url
from codes.web.devotions.views import sheet 
from codes.web.devotions.views import editor
from codes.web.devotions.views import editted
from codes.web.devotions.views import create
from codes.web.devotions.views import created
from codes.web.devotions.views import list


urlpatterns = [
    url(r'^view/(?P<object_id>([a-zA-Z0-9%\s\'-])+)/$', sheet, name="sheet"),
    url(r'^edit/(?P<object_id>([a-zA-Z0-9%\s\'-])+)/$', editor, name="editor"),
    url(r'^editted/$', editted, name="editted"),
    url(r'^create/$', create, name="create"),
    url(r'^created/$', created, name="created"),
    url(r'^list/$', list, name="list")
]