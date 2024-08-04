from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["DELETE"])
def route_3(request):
    return HttpResponse("I'm a DELETE request")

