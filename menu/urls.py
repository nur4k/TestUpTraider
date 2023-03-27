from django.urls import path

from menu.views import home


urlpatterns = [
    path('home/', home, {'name': 'Home'}, name='home'),
    path('company/', home, {'name': 'About company'}, name='company'),
    path('development/', home, {'name': 'Development'}, name='development'),
    path('development/python/django', home, {'name': 'Development Python/Django'}, name='development_python_django'),
    path('development/python/tornado', home, {'name': 'Development Python/Tornado'}, name='development_python_tornado'),
    path('prices/', home, {'name': 'Prices'}, name='prices'),
]