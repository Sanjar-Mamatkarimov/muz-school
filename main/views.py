from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SiteSettings, Department, Event, Application, Reward, Teacher, Review, GalleryImage
from .forms import ApplicationForm, ReviewForm

def get_context():
    """Базовый контент для всех страниц"""
    return {
        'settings': SiteSettings.objects.first(),
        'departments': Department.objects.all(),
        'events': Event.objects.all(),
        'rewards': Reward.objects.all().order_by('order'),
        'teachers': Teacher.objects.all().order_by('order'),
        'reviews': Review.objects.filter(is_published=True).order_by('-created_at'),
    }

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        instrument = request.POST.get('instrument')

        Application.objects.create(
            name=name,
            phone=phone,
            instrument=instrument
        )
        messages.success(request, 'Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.')
        return redirect('home') 

    context = get_context()
    return render(request, 'home.html', context)

def teachers(request):
    context = get_context()
    return render(request, 'teachers.html', context)

def departments(request):
    context = get_context()
    return render(request, 'departments.html', context)

def events(request):
    context = get_context()
    return render(request, 'events.html', context)

def rewards(request):
    context = get_context()
    return render(request, 'rewards.html', context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        instrument = request.POST.get('instrument', '')

        if name and phone:
            Application.objects.create(
                name=name,
                phone=phone,
                instrument=instrument
            )
            messages.success(request, 'Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.')
            return redirect('contacts')
        else:
            messages.error(request, 'Пожалуйста, заполните обязательные поля.')

    context = get_context()
    return render(request, 'contacts.html', context)


def reviews(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо за ваш отзыв! Он будет опубликован после модерации.')
            return redirect('reviews')
    else:
        form = ReviewForm()
    
    context = get_context()
    context['form'] = form
    return render(request, 'reviews.html', context)


def gallery(request):
    context = get_context()
    context['gallery_images'] = GalleryImage.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'gallery.html', context)
