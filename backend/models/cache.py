# Epic Title: As a system architect, I want to implement caching strategies in both frontend and backend, so that the system can handle a larger number of requests efficiently.

class Cache:
    def __init__(self, key: str, value: str, ttl: int):
        self.key = key
        self.value = value
        self.ttl = ttl