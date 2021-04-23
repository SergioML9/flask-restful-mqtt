from flask import current_app

def get_mqtt_session():
    try:
        return current_app.extensions["mqtt"]["session"]
    except KeyError:
        raise RuntimeError(
            "You must initiliaze an MQTT session"
        )