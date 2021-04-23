from flask_mqtt import Mqtt
from flask import current_app, _app_ctx_stack


class FlaskRestfulMQTT(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        self.app = app

        app.extensions = getattr(app, "extensions", {})

        if "flask-restful-mqtt" not in app.extensions:
            app.extensions["flask-restful-mqtt"] = {}

        #app.config.setdefault('AGRAPH_HOST', 'localhost')
        #app.config.setdefault('AGRAPH_PORT', '10035')
        
        
        session = self.connect(app)
        s = {"app": app, "session": session}
        app.extensions["flask-restful-mqtt"] = s

        app.teardown_appcontext(self.teardown)


    def connect(self, app):
        #app.config['MQTT_BROKER_URL'] = app.config['MOSQUITTO_HOST']
        #app.config['MQTT_BROKER_PORT'] = int(app.config['MOSQUITTO_PORT'])
        #flask_app.config['MQTT_USERNAME'] = 'user'
        #flask_app.config['MQTT_PASSWORD'] = 'secret'
        #app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
        mqtt = Mqtt(app)

        print('Create the mqtt session')
        return mqtt

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'flaskrestfulmqtt'): #
            ctx.flaskrestfulmqtt.close()

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'flaskrestfulmqtt'):
                ctx.flaskrestfulmqtt = self.connect()
            return ctx.flaskrestfulmqtt