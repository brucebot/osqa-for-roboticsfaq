#!/usr/bin/python2.6
import sys, os

sys.path.insert(0, "/home2/robotinc/.local/lib/python2.6")
sys.path.insert(0,"/home2/robotinc/.local/lib/python2.6/site-packages/django")
#sys.path.append('/home2/robotinc/public_html/roboticsfaq')
os.chdir("/home2/robotinc/public_html/roboticsfaq")

os.environ['DJANGO_SETTINGS_MODULE'] = "roboticsfaq.settings"

from flup.server.fcgi import WSGIServer
from django.core.handlers.wsgi import WSGIHandler
WSGIServer(WSGIHandler()).run()
#from django.core.servers.fastcgi import runfastcgi
#runfastcgi(method="threaded", daemonize="false")
