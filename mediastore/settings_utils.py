import os
import sys
import urlparse

def set_default_env(**kwargs):
    for key in kwargs:
        if not key in os.environ:
            os.environ[key] = kwargs[key]

def set_default_db(default):
    set_default_env(DATABASE_URL=default)
    url = os.environ['DATABASE_URL']
    if url.upper() == url:
        # The environment variable is naming another environment variable,
        # whose value we should retrieve.
        os.environ['DATABASE_URL'] = os.environ[url]

def parse_secure_proxy_ssl_header(field):
    name, value = field.split(':')
    return ('HTTP_%s' % name.upper().replace('-', '_'), value.strip())

def parse_storage_backend_url(url):
    info = urlparse.urlparse(url)
    s = {}
    if info.scheme == 's3':
        s['DEFAULT_FILE_STORAGE'] = 'storages.backends.s3boto.S3BotoStorage'
        if info.username:
            s['AWS_ACCESS_KEY_ID'] = info.username
        if info.password:
            s['AWS_SECRET_ACCESS_KEY'] = info.password
        s['AWS_STORAGE_BUCKET_NAME'] = info.hostname
    else:
        raise ValueError('unknown scheme for storage backend url: %s' % url)
    return s
