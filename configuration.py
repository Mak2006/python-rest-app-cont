class BaseConfig(object):
    'Base config class FOR ALL ENvironments'
    SECRET_KEY = 'A random secret key'
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = 'my value'


class ProductionConfig(BaseConfig):
    'Production specific config'
    # set debug to false
    DEBUG = False
    # take the key from secret file
    SECRET_KEY = open('/dir/secret/file').read()


class StagingConfig(BaseConfig):
    'Staging specific config'
    DEBUG = True
    # Use the same secret_key as the base config


class DevelopmentConfig(BaseConfig):
    'Development environment specific config'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Another random secret key'