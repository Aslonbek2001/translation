from django.urls import path
from .views import TranslateView, DocumentView

urlpatterns = [
    path("", TranslateView.as_view(), name="translate"),
    path("docs/", DocumentView.as_view(), name="document"),
]