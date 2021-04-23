from flask_restful_mqtt.internal_utils import get_mqtt_session

def get_session():
    return get_mqtt_session()