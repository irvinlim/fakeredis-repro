from time import time

from fakeredis import FakeStrictRedis
from redis import StrictRedis

config = {
    'host': 'redis',
    'port': 6379,
}


def main():
    redis = StrictRedis(**config)
    fakeredis = FakeStrictRedis()
    redis.flushall()
    fakeredis.flushall()

    print '[*] FakeRedis BLPOP:'
    now = time()
    fakeredis.blpop('hello_world', 10)
    print '[*] Took %.2f seconds' % (time() - now)

    print '[*] Redis BLPOP:'
    now = time()
    redis.blpop('hello_world', 10)
    print '[*] Took %.2f seconds' % (time() - now)


if __name__ == '__main__':
    main()
