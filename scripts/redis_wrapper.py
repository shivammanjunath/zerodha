import redis

rd_connection = redis.StrictRedis('127.0.0.1', 6379, charset = "utf-8", decode_responses = True, db = 0)


def save_data(key, value):
    rd_connection.set(key, value)


def get_data(key):
    return rd_connection.get(key)


def delete_data(key):
    rd_connection.delete(key)
