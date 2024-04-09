# middlewares/post_login_redirect_middleware.py

from django.shortcuts import redirect

class PostLoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        redirect_to = request.session.pop('redirect_to', None)
        if redirect_to and response.status_code == 200:
            return redirect(redirect_to)
        return response
