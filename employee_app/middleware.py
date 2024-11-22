import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class CustomCorsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        logger.info("Request Headers: %s", request.META)  # Log all request headers
        origin = request.META.get('HTTP_ORIGIN')
        if origin:
            response['Access-Control-Allow-Origin'] = origin
            response['Access-Control-Allow-Credentials'] = 'true'
        return response
