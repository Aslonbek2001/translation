from django.urls import path, include
from .views import TranslateView
urlpatterns = [
    path("", TranslateView.as_view(), name="translate")
]