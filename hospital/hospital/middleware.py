from django.utils import timezone
from django.contrib.auth import logout
from django.conf import settings
from django.http import HttpResponseRedirect


class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            if last_activity is not None:
                elapsed_time = timezone.now() - last_activity
                if elapsed_time.total_seconds() > settings.SESSION_COOKIE_AGE:
                    logout(request)
            request.session['last_activity'] = timezone.now()
        response = self.get_response(request)
        return response