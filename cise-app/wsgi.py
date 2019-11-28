import sys
import site

site.addsitedir('/var/www/cise/venv/lib/python3.6/site-packages')

sys.path.insert(0, '/var/www/cise')

from app import app as application
