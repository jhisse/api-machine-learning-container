import falcon

from ping_handler import Ping
from predict_handler import Predict


def create_api():
    api = falcon.API()

    # Routes
    api.add_route('/ping', Ping())
    api.add_route('/predict', Predict())

    return api


# Init app
app = create_api()

if __name__ == '__main__':
    from wsgiref import simple_server

    httpd = simple_server.make_server('0.0.0.0', 8000, app)
    httpd.serve_forever()
