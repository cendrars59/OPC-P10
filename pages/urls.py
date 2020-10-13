from django.urls import path

from . import views

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path("", views.home, name="pages-home"),
    path("mentions", views.mentions, name="pages-mentions"),
    path('sentry-debug/', trigger_error),
]



