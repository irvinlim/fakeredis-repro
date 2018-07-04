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

    print '[+] FakeRedis BLPOP:'
    now = time()
    popped = fakeredis.blpop('hello_world', 10)
    print '[*] Took %.2f seconds' % (time() - now)
    print '[*] Popped value:', popped
    print

    print '[+] Redis BLPOP:'
    now = time()
    popped = redis.blpop('hello_world', 10)
    print '[*] Took %.2f seconds' % (time() - now)
    print '[*] Popped value:', popped


if __name__ == '__main__':
    main()
