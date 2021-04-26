from redis import StrictRedis


class Config(object):
    """项目的配置"""
    DEBUG = True

    # 设置48字符的随机密匙
    SECRET_KEY = "SECRET_KEY = Ke0McAKwJlAy+/7tgL2pY7pqRZfT3gEfo27JXZMXQ0M8frNLgba3djNBx4O3xiVW"
    # 配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置Redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # Session保存设置  指定 session 保存到 redis 中
    SESSION_TYPE = "redis"
    # 开启session签名  让 cookie 中的 session_id 被加密签名处理
    SESSION_USE_SIGER = True
    # 指定Session 保存的redis，不指定他会帮你指定，这样redis就不能设置端口，地址了
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = True
    # 设置过期时间 源代码中默认是31 天
    PERMANENT_SESSION_LIFETIME = 86400 * 2