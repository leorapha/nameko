from nameko.web.handlers import http



class HttpService:

    name = 'http_service'

    @http('GET', '/get/<int:value>')
    def get_method(self, request, value):
        return 'Vixe: ' + str(value)