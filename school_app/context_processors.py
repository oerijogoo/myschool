from .models import SchoolSettings, NavbarAdvert


def school_settings(request):
    try:
        settings = SchoolSettings.objects.latest('created_at')
    except SchoolSettings.DoesNotExist:
        settings = None

    navbar_adverts = NavbarAdvert.objects.filter(is_active=True).order_by('order')

    return {
        'school_settings': settings,
        'navbar_adverts': navbar_adverts
    }