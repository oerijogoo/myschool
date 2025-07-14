# school_app/forms.py
from django import forms
from .models import SchoolSetting, HeroImage, NavbarAdvert, Page, Section, Subsection, News, Event, Achievement, SchoolCalendar, FeeStructure, GalleryImage

class SchoolSettingForm(forms.ModelForm):
    class Meta:
        model = SchoolSetting
        fields = '__all__'
        widgets = {
            'aim': forms.Textarea(attrs={'rows': 4}),
            'history': forms.Textarea(attrs={'rows': 4}),
            'google_map_embed': forms.Textarea(attrs={'rows': 4}),
        }

class HeroImageForm(forms.ModelForm):
    class Meta:
        model = HeroImage
        fields = '__all__'

class NavbarAdvertForm(forms.ModelForm):
    class Meta:
        model = NavbarAdvert
        fields = '__all__'

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

class SubsectionForm(forms.ModelForm):
    class Meta:
        model = Subsection
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = '__all__'

class SchoolCalendarForm(forms.ModelForm):
    class Meta:
        model = SchoolCalendar
        fields = '__all__'

class FeeStructureForm(forms.ModelForm):
    class Meta:
        model = FeeStructure
        fields = '__all__'

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = '__all__'