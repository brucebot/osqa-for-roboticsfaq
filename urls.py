from django.conf.urls.defaults import *
from django.utils.translation import ugettext as _
from django.conf import settings

urlpatterns = patterns('',
    (r'^admin_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/usr/lib/pymodules/python2.6/django/contrib/admin/media', 'show_indexes': True}),
    (r'^%s' % settings.FORUM_SCRIPT_ALIAS, include('forum.urls')),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )

