from django.urls import path, include
from . import views
from . import views_static as vs

urlpatterns = [
    # home page
    path("", vs.home, name='home'),

    # Sign in form
    path('sign-in', vs.sign_in, name='sign_in'),

    # Major User features
    path('dashboard', views.dashboard, name='dashboard'),
    path('monitor_destinations', views.monitor_destinations, name='monitor'),
    path("time_out", views.time_out, name='time_out'),
    path("time_in", views.time_in, name='time_in'),
    path("change_location", views.change_location, name='change_location'),

    # Static Pages required for OAuth and SEO
    path('about/', vs.about, name='about'),
    path('contact/', vs.contact, name='contact'),
    path('help/', vs.help, name='help'),
    path('robots.txt', vs.robots, name='robots'),
    path('privacy/', vs.privacy, name='privacy'),
    path('terms/', vs.terms, name='terms'),

]