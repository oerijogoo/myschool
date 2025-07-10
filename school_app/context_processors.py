# school_app/context_processors.py

from .models import SchoolInfo, Page

def school_info(request):
    school = SchoolInfo.objects.first()
    menu_pages = Page.objects.filter(is_published=True, show_in_menu=True).order_by('menu_order')
    return {
        'school': school,
        'menu_pages': menu_pages,
    }