import sae
from Portal_site import wsgi

application = sae.create_wsgi_app(wsgi.application)
