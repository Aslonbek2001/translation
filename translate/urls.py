from django.urls import path
from .views import TranslateView, DocumentView, IndexView, FAQApiView, StarsApiView

urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("tarjima/", TranslateView.as_view(), name="translate"),
    path("docs/", DocumentView.as_view(), name="document"),
    path("quetions/", FAQApiView.as_view(), name="faqs"),
    path("stars/", StarsApiView.as_view(), name="stars"),
]