from django.http import JsonResponse

def getRoutes(response):
    routes = [
        'GET /api',
        'GET/ api /rooms',
        'GET / api / rooms/:id'
    ]
    return JsonResponse(routes , safe=False)

