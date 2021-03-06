import os
from django.test import TestCase
from mock import patch

from ..settings_utils import set_default_env, set_default_db, \
                             parse_secure_proxy_ssl_header, \
                             parse_storage_backend_url

class SetDefaultEnvTests(TestCase):
    def test_sets_default_values(self):
        with patch.dict(os.environ, {'TEST_FOO': ''}):
            del os.environ['TEST_FOO']
            set_default_env(TEST_FOO='bar')
            self.assertEqual(os.environ['TEST_FOO'], 'bar')

    def test_does_not_overwrite_existing_values(self):
        with patch.dict(os.environ, {'TEST_FOO': ''}):
            set_default_env(TEST_FOO='bar')
            self.assertEqual(os.environ['TEST_FOO'], '')

class SetDefaultDbTests(TestCase):
    def test_follows_env_vars(self):
        with patch.dict(os.environ, {'DATABASE_URL': 'FOO', 'FOO': 'bar'}):
            set_default_db('meh')
            self.assertEqual(os.environ['DATABASE_URL'], 'bar')

    def test_does_not_overwrite_existing_value(self):
        with patch.dict(os.environ, {'DATABASE_URL': 'foo'}):
            set_default_db('meh')
            self.assertEqual(os.environ['DATABASE_URL'], 'foo')

    def test_sets_default_value(self):
        with patch.dict(os.environ, {'DATABASE_URL': ''}):
            del os.environ['DATABASE_URL']
            set_default_db('meh')
            self.assertEqual(os.environ['DATABASE_URL'], 'meh')

class ParseSecureProxySslHeaderTests(TestCase):
    def test_basic_functionality(self):
        self.assertEqual(
            parse_secure_proxy_ssl_header('X-Forwarded-Proto: https'),
            ('HTTP_X_FORWARDED_PROTO', 'https')
        )

class ParseStorageBackendUrlTests(TestCase):
    def test_accepts_s3(self):
        self.assertEqual(parse_storage_backend_url('s3://foo:bar@boop'), {
            'DEFAULT_FILE_STORAGE': 'storages.backends.s3boto.S3BotoStorage',
            'AWS_ACCESS_KEY_ID': 'foo',
            'AWS_SECRET_ACCESS_KEY': 'bar',
            'AWS_STORAGE_BUCKET_NAME': 'boop'
        })
