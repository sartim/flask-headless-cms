from gevent import monkey
from gevent.pywsgi import WSGIServer
from werkzeug.contrib.fixers import ProxyFix
from skeleton.app import *

if __name__ == "__main__":
    monkey.patch_all()
    # fixes the X-Real-IP header
    app.wsgi_app = ProxyFix(app.wsgi_app)
    http_server = WSGIServer(('', 5000), app.wsgi_app)
    http_server.serve_forever()
