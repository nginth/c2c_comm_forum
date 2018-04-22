import os
from flaskbb import create_app
from flaskbb.utils.helpers import ReverseProxyPathFix

_basepath = os.path.dirname(os.path.abspath(__file__))

# will throw an error if the config doesn't exist
flaskbb = create_app(config='flaskbb.cfg')
flaskbb.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres://flaskbb@localhost:5432/flaskbb')

#  Uncomment to use the middleware
#flaskbb.wsgi_app = ReverseProxyPathFix(flaskbb.wsgi_app)
