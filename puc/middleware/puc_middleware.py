from user_auth.models import User
from django.utils.deprecation import MiddlewareMixin

class PucMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        following code for updating the User object as its not contains the
        proxy methods.
        see. user_auth/models.py
        """

        """following code for handling for unauthenticated requests"""
        if request.user.is_anonymous:
            return None

        """override User instance with Proxy Class instance to get
        all proxy method in object"""
        request.user = User.objects.get(pk=request.user.id)
        return None
