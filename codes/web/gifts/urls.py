
from django.conf.urls import url
from codes.web.gifts.views import sheet
from codes.web.gifts.views import editor
from codes.web.gifts.views import editted
from codes.web.gifts.views import create
from codes.web.gifts.views import created
from codes.web.gifts.views import list


urlpatterns = [
    url(r'^view/(?P<object_id>(.)+)/$', sheet, name="sheet"),
    url(r'^edit/(?P<object_id>(.)+)/$', editor, name="editor"),
    url(r'^editted/$', editted, name="editted"),
    url(r'^create/$', create, name="create"),
    url(r'^created/$', created, name="created"),
    url(r'^list/$', list, name="list")
]