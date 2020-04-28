import gevent
from gevent import monkey;

monkey.patch_all()
import urllib2


def f(url):
    print 'GET: %s' % url
    resp = urllib2.urlopen(url)
    data = resp.read()
    print '[%d] bytes received from %s\n' % (len(data), url)


gevent.joinall([
    gevent.spawn(f, 'http://www.cnblogs.com/kaituorensheng/'),
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.baidu.com'),
])
