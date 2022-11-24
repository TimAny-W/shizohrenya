from django.conf import settings

def context_processor(request):
    return {'media_url': settings.STATIC_ROOT}