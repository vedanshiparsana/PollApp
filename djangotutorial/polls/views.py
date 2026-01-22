from django.http import HttpResponse


def index(request):
    return HttpResponse("Helloooo, world. You're at the polls index.")