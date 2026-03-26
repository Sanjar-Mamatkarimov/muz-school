from django import forms
from .models import Application, Review

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'phone', 'instrument', 'age', 'message']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш отзыв', 'rows': 5}),
            'rating': forms.RadioSelect(attrs={'class': 'form-check-input'}, choices=[(i, f'{i} звезда(ы)') for i in range(1, 6)])
        }

