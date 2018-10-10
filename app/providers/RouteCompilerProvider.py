from masonite.routes import Route
from masonite.provider import ServiceProvider


class RouteCompilerProvider(ServiceProvider):

    wsgi = False

    def register(self):
        pass

    def boot(self, route: Route):
        route.compile('foo', r'[a-z]')