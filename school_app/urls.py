# school_app/urls.py

from django.urls import path
from . import views
from .views import (
    NewsListView, NewsDetailView, EventListView, EventDetailView,
    AchievementListView, AchievementDetailView, ClassListView, ClassDetailView,
    TeacherListView, TeacherDetailView, GalleryView
)

urlpatterns = [
    # Frontend URLs
    path('', views.home, name='home'),
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('achievements/', AchievementListView.as_view(), name='achievement-list'),
    path('achievements/<int:pk>/', AchievementDetailView.as_view(), name='achievement-detail'),
    path('classes/', ClassListView.as_view(), name='class-list'),
    path('classes/<int:pk>/', ClassDetailView.as_view(), name='class-detail'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('page/<slug:slug>/', views.page_detail, name='page-detail'),

    # Admin URLs
    path('admin/school-info/', views.SchoolInfoUpdateView.as_view(), name='admin-school-info'),
    path('admin/hero-images/', views.HeroImageListView.as_view(), name='admin-hero-images'),
    path('admin/hero-images/add/', views.HeroImageCreateView.as_view(), name='admin-hero-image-add'),
    path('admin/hero-images/<int:pk>/edit/', views.HeroImageUpdateView.as_view(), name='admin-hero-image-edit'),
    path('admin/hero-images/<int:pk>/delete/', views.HeroImageDeleteView.as_view(), name='admin-hero-image-delete'),

    # Similarly add URLs for other admin CRUD operations
    # Following the same pattern as above for each model

    # Admin URLs
    path('admin/school-info/', views.SchoolInfoUpdateView.as_view(), name='admin-school-info'),

    # Hero Images
    path('admin/hero-images/', views.HeroImageListView.as_view(), name='admin-hero-images'),
    path('admin/hero-images/add/', views.HeroImageCreateView.as_view(), name='admin-hero-image-add'),
    path('admin/hero-images/<int:pk>/edit/', views.HeroImageUpdateView.as_view(), name='admin-hero-image-edit'),
    path('admin/hero-images/<int:pk>/delete/', views.HeroImageDeleteView.as_view(), name='admin-hero-image-delete'),

    # News
    path('admin/news/', views.NewsListView.as_view(), name='admin-news-list'),
    path('admin/news/add/', views.NewsCreateView.as_view(), name='admin-news-add'),
    path('admin/news/<int:pk>/edit/', views.NewsUpdateView.as_view(), name='admin-news-edit'),
    path('admin/news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='admin-news-delete'),

    # Events
    path('admin/events/', views.EventAdminListView.as_view(), name='admin-event-list'),
    path('admin/events/add/', views.EventCreateView.as_view(), name='admin-event-add'),
    path('admin/events/<int:pk>/edit/', views.EventUpdateView.as_view(), name='admin-event-edit'),
    path('admin/events/<int:pk>/delete/', views.EventDeleteView.as_view(), name='admin-event-delete'),

    # Achievements
    path('admin/achievements/', views.AchievementAdminListView.as_view(), name='admin-achievement-list'),
    path('admin/achievements/add/', views.AchievementCreateView.as_view(), name='admin-achievement-add'),
    path('admin/achievements/<int:pk>/edit/', views.AchievementUpdateView.as_view(), name='admin-achievement-edit'),
    path('admin/achievements/<int:pk>/delete/', views.AchievementDeleteView.as_view(), name='admin-achievement-delete'),

    # Classes
    path('admin/classes/', views.ClassAdminListView.as_view(), name='admin-class-list'),
    path('admin/classes/add/', views.ClassCreateView.as_view(), name='admin-class-add'),
    path('admin/classes/<int:pk>/edit/', views.ClassUpdateView.as_view(), name='admin-class-edit'),
    path('admin/classes/<int:pk>/delete/', views.ClassDeleteView.as_view(), name='admin-class-delete'),

    # Teachers
    path('admin/teachers/', views.TeacherAdminListView.as_view(), name='admin-teacher-list'),
    path('admin/teachers/add/', views.TeacherCreateView.as_view(), name='admin-teacher-add'),
    path('admin/teachers/<int:pk>/edit/', views.TeacherUpdateView.as_view(), name='admin-teacher-edit'),
    path('admin/teachers/<int:pk>/delete/', views.TeacherDeleteView.as_view(), name='admin-teacher-delete'),

    # Adverts
    path('admin/adverts/', views.AdvertAdminListView.as_view(), name='admin-advert-list'),
    path('admin/adverts/add/', views.AdvertCreateView.as_view(), name='admin-advert-add'),
    path('admin/adverts/<int:pk>/edit/', views.AdvertUpdateView.as_view(), name='admin-advert-edit'),
    path('admin/adverts/<int:pk>/delete/', views.AdvertDeleteView.as_view(), name='admin-advert-delete'),

    # Gallery Categories
    path('admin/gallery-categories/', views.GalleryCategoryAdminListView.as_view(), name='admin-gallerycategory-list'),
    path('admin/gallery-categories/add/', views.GalleryCategoryCreateView.as_view(), name='admin-gallerycategory-add'),
    path('admin/gallery-categories/<int:pk>/edit/', views.GalleryCategoryUpdateView.as_view(),
         name='admin-gallerycategory-edit'),
    path('admin/gallery-categories/<int:pk>/delete/', views.GalleryCategoryDeleteView.as_view(),
         name='admin-gallerycategory-delete'),

    # Gallery Images
    path('admin/gallery-images/', views.GalleryImageAdminListView.as_view(), name='admin-galleryimage-list'),
    path('admin/gallery-images/add/', views.GalleryImageCreateView.as_view(), name='admin-galleryimage-add'),
    path('admin/gallery-images/<int:pk>/edit/', views.GalleryImageUpdateView.as_view(), name='admin-galleryimage-edit'),
    path('admin/gallery-images/<int:pk>/delete/', views.GalleryImageDeleteView.as_view(),
         name='admin-galleryimage-delete'),

    # Pages
    path('admin/pages/', views.PageAdminListView.as_view(), name='admin-page-list'),
    path('admin/pages/add/', views.PageCreateView.as_view(), name='admin-page-add'),
    path('admin/pages/<int:pk>/edit/', views.PageUpdateView.as_view(), name='admin-page-edit'),
    path('admin/pages/<int:pk>/delete/', views.PageDeleteView.as_view(), name='admin-page-delete'),
]