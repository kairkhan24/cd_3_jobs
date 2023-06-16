from django.urls import path

from .views import BookCreateView


urlpatterns = [
    path('book-create/', BookCreateView.as_view())
]
