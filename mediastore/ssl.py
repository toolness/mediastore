from django.http import HttpResponsePermanentRedirect
from django.core.exceptions import MiddlewareNotUsed

from django.conf import settings

class SslMiddleware(object):
    def __init__(self):
        if not getattr(settings, 'SECURE_PROXY_SSL_HEADER', None):
            raise MiddlewareNotUsed()

class RedirectToHttpsMiddleware(SslMiddleware):
    def process_request(self, request):
        if not request.is_secure():
            url = 'https://%s%s' % (request.get_host(), request.path)
            return HttpResponsePermanentRedirect(url)

class HstsMiddleware(SslMiddleware):
    def process_response(self, request, response):
        response["Strict-Transport-Security"] = "max-age=31536000; " \
                                                "includeSubdomains"
        return response
