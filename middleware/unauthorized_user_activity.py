from django.conf import settings
from rich.logging import RichHandler
import logging


class UnauthorizedUserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger("rich")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(RichHandler(show_path=False))

    def __call__(self, request):
        response = self.get_response(request)
        if settings.UNAUTHORIZED_USER_ACTIVITY and not request.user.is_authenticated:
            user_ip = self.get_client_ip(request)
            url = request.build_absolute_uri()
            self.logger.info(f"Unauthorized user IP: {user_ip} URL: {url} Type: {request.method}")
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
