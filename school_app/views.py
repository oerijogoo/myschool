from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    hero_images = HeroImage.objects.filter(is_active=True).order_by('order')
    sections = Section.objects.filter(section_type='home', is_active=True).order_by('order')
    news = News.objects.filter(is_active=True).order_by('-created_at')[:4]
    events = Event.objects.filter(is_active=True).order_by('date')[:4]
    achievements = Achievement.objects.filter(is_active=True).order_by('-date_achieved')[:3]

    context = {
        'hero_images': hero_images,
        'sections': sections,
        'news': news,
        'events': events,
        'achievements': achievements,
        'page': 'home'
    }
    return render(request, 'school_app/home.html', context)


def about(request):
    sections = Section.objects.filter(section_type='about', is_active=True).order_by('order')
    context = {
        'sections': sections,
        'page': 'about'
    }
    return render(request, 'school_app/about.html', context)


def academics(request):
    sections = Section.objects.filter(section_type='academics', is_active=True).order_by('order')
    context = {
        'sections': sections,
        'page': 'academics'
    }
    return render(request, 'school_app/academics.html', context)


def admissions(request):
    sections = Section.objects.filter(section_type='admissions', is_active=True).order_by('order')
    context = {
        'sections': sections,
        'page': 'admissions'
    }
    return render(request, 'school_app/admissions.html', context)


def news(request):
    news_list = News.objects.filter(is_active=True).order_by('-created_at')
    context = {
        'news_list': news_list,
        'page': 'news'
    }
    return render(request, 'school_app/news.html', context)


def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    context = {
        'news': news_item,
        'page': 'news'
    }
    return render(request, 'school_app/news_detail.html', context)


def events(request):
    events_list = Event.objects.filter(is_active=True).order_by('date')
    context = {
        'events': events_list,
        'page': 'events'
    }
    return render(request, 'school_app/events.html', context)


def achievements(request):
    achievements_list = Achievement.objects.filter(is_active=True).order_by('-date_achieved')
    context = {
        'achievements': achievements_list,
        'page': 'achievements'
    }
    return render(request, 'school_app/achievements.html', context)


def gallery(request):
    # Get all active gallery items ordered by their specified order
    gallery_items = GalleryItem.objects.filter(is_active=True).order_by('order')

    # Group items by category for filtering
    categories = dict(GalleryItem.CATEGORY_CHOICES)

    context = {
        'gallery_items': gallery_items,
        'categories': categories,
        'page': 'gallery'
    }
    return render(request, 'school_app/gallery.html', context)


def contact(request):
    sections = Section.objects.filter(section_type='contact', is_active=True).order_by('order')
    context = {
        'sections': sections,
        'page': 'contact'
    }
    return render(request, 'school_app/contact.html', context)


def calendar(request):
    calendars = SchoolCalendar.objects.filter(is_active=True).order_by('-year')
    context = {
        'calendars': calendars,
        'page': 'calendar'
    }
    return render(request, 'school_app/calendar.html', context)


def fees(request):
    fee_structures = FeeStructure.objects.filter(is_active=True).order_by('-created_at')
    context = {
        'fee_structures': fee_structures,
        'page': 'fees'
    }
    return render(request, 'school_app/fees.html', context)