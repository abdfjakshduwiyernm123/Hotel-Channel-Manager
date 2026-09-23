from django.urls import path

from .views import Views

urlpatterns: list[str] = [
    path("", Views.home_page, name="log-in"),
    path("managers-report", Views.managers_report, name="managers-report"),
    path("owners-report", Views.owners_report, name="owners-report"),
]
