# Configs for Flask App.

class BaseConfig(object):
    DEBUG = True
    TESTING = True 
    ENV = "Development"
    SERVER_NAME = "0.0.0.0:5000"

class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = "Production"
    JSONIFY_PRETTYPRINT_REGULAR = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True

class TestingConfig(BaseConfig):
    # Disable CSRF tokens in the Forms (only valid for testing purposes!)
    WTF_CSRF_ENABLED = False
    TESTING = True
    # Bcrypt algorithm hashing rounds (reduced for testing purposes only!)
    BCRYPT_LOG_ROUNDS = 4
