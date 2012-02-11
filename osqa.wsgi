#!/usr/bin/python
import os
import sys
sys.path.append('/var/www/')
sys.path.append('/var/www/rbfaq')
os.environ['DJANGO_SETTINGS_MODULE'] = 'rbfaq.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
