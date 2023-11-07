class Config(object):
    DEBUG = False
    TESTING = False
    



    # SEQUIRITY_PASSWORD_SALT = 'thisisaltt'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # WTF_CSRF_ENABLED = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'


# class TestingConfig(Congfig):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///../databases/test.db'



