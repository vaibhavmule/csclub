""" CSRF Middleware """

from masonite.exceptions import InvalidCSRFToken
from masonite.middleware import CsrfMiddleware as Middleware


class CsrfMiddleware(Middleware):
    """ Verify CSRF Token Middleware """

    exempt = []

    def __verify_csrf_token(self):
        """
        Verify si csrf token in post is valid.
        """

        if self.request.is_post() and not self.__in_exempt():
            token = self.request.input('__token')
            if not self.csrf.verify_csrf_token(token):
                raise InvalidCSRFToken("Invalid CSRF token.")
        else:
            if self.request.get_cookie('csrf_token', decrypt=False):
                return self.request.get_cookie('csrf_token', decrypt=False)
            token = self.csrf.generate_csrf_token()

        return token
