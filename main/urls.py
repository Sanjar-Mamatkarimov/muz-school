from django.urls import path
from .views import home, teachers, departments, events, rewards, contacts, reviews, gallery

urlpatterns = [
    path('', home, name='home'),
    path('teachers/', teachers, name='teachers'),
    path('departments/', departments, name='departments'),
    path('events/', events, name='events'),
    path('rewards/', rewards, name='rewards'),
    path('contacts/', contacts, name='contacts'),
    path('reviews/', reviews, name='reviews'),
    path('gallery/', gallery, name='gallery'),
]