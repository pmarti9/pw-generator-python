import redis

class RedisConfig:
    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db

    def get_redis_connection(self):
        return redis.Redis(host=self.host, port=self.port, db=self.db)