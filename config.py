class Config(object):
    """
    Common configurations
    """

    DEBUG = True

    RECAPTCHA_PUBLIC_KEY = '6LdYIDcUAAAAAEE3N3tNqcYu50MJSTlGA5lwu5Pl'
    RECAPTCHA_PRIVATE_KEY = '6LdYIDcUAAAAAD8ayN_2Mkhauh_-MdK12XxdTLEo'


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
