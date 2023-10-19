import redis
import json

rd = redis.StictRedis(port=6379, db=0)


class Redis:
    def set(cache_key, input_data):
        dumped_data = json.dumps(input_data)
        rd.set(cache_key, dumped_data, 45)
        return True

    def get(cache_key):
        cache_data = rd.get(cache_key)
        if not cache_data:
            return False
        cache_data_json = json.load(cache_data)
        return cache_data_json

