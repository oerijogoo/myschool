from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class SchoolSettings(models.Model):
    school_name = models.CharField(max_length=200, default="Kenyan Excellence Academy")
    logo = CloudinaryField('logo', folder='settings', blank=True, null=True)
    address = models.TextField(default="Nairobi, Kenya")
    phone = models.CharField(max_length=20, default="+254 700 000 000")
    email = models.EmailField(default="info@school.ac.ke")
    motto = models.CharField(max_length=200, default="Striving for Excellence")
    aim = RichTextField(default="Our aim is to provide quality education...")
    history = RichTextField(default="Founded in 2000...")
    google_map_embed = models.TextField(blank=True, null=True, help_text="Paste Google Maps embed code here")
    navbar_color = ColorField(default='#006600', verbose_name="Navbar Color")
    footer_color = ColorField(default='#333333', verbose_name="Footer Color")
    navbar_font_color = ColorField(default='#ffffff', verbose_name="Navbar Font Color")
    footer_font_color = ColorField(default='#ffffff', verbose_name="Footer Font Color")
    body_font = models.CharField(max_length=100, default="'Helvetica Neue', Helvetica, Arial, sans-serif")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "School Settings"

    class Meta:
        verbose_name = "School Setting"
        verbose_name_plural = "School Settings"

class HeroImage(models.Model):
    TRANSITION_CHOICES = [
        ('fade', 'Fade'),
        ('zoom', 'Zoom'),
        ('flip', 'Flip'),
        ('slide', 'Slide'),
        ('carousel', 'Carousel'),
        ('flip3d', 'Flip 3D'),
        ('mask_reveal', 'Mask Reveal'),
        ('ken_burns', 'Ken Burns'),
    ]

    title = models.CharField(max_length=200)
    image = CloudinaryField('image', folder='hero_images')
    caption = models.CharField(max_length=200, blank=True, null=True)
    transition_style = models.CharField(max_length=50, choices=TRANSITION_CHOICES, default='fade')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = "Hero Image"
        verbose_name_plural = "Hero Images"

class Section(models.Model):
    SECTION_TYPE_CHOICES = [
        ('home', 'Home Page'),
        ('about', 'About Page'),
        ('academics', 'Academics Page'),
        ('admissions', 'Admissions Page'),
        ('news', 'News Page'),
        ('events', 'Events Page'),
        ('achievements', 'Achievements Page'),
        ('gallery', 'Gallery Page'),
        ('contact', 'Contact Page'),
    ]

    title = models.CharField(max_length=200)
    section_type = models.CharField(max_length=50, choices=SECTION_TYPE_CHOICES)
    content = RichTextField(blank=True, null=True)
    background_color = ColorField(default='#ffffff', verbose_name="Background Color")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.section_type} - {self.title}"

    class Meta:
        ordering = ['order']

class SubSection(models.Model):
    section = models.ForeignKey(Section, related_name='subsections', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    image = CloudinaryField('image', folder='subsections', blank=True, null=True)
    background_color = ColorField(default='#f8f9fa', verbose_name="Background Color")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.section.title} - {self.title}"

    class Meta:
        ordering = ['order']

class News(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = CloudinaryField('image', folder='news', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    date_achieved = models.DateField()
    image = CloudinaryField('image', folder='achievements', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class SchoolCalendar(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    calendar_file = CloudinaryField('file', folder='calendars', resource_type='raw')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

class FeeStructure(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    fee_file = CloudinaryField('file', folder='fee_structures', resource_type='raw')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class NavbarAdvert(models.Model):
    text = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)
    background_color = ColorField(default='#ffcc00', verbose_name="Background Color")
    text_color = ColorField(default='#000000', verbose_name="Text Color")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['order']
        verbose_name = "Navbar Advert"
        verbose_name_plural = "Navbar Adverts"

class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Gallery Categories"
        ordering = ['order']

    def __str__(self):
        return self.name

class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ('events', 'Events'),
        ('sports', 'Sports'),
        ('academics', 'Academics'),
        ('facilities', 'Facilities'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='events')
    image = CloudinaryField('image', folder='gallery')
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title