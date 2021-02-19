from django.urls import path
from .views import MainPageView, FomoView

urlpatterns = [
    path('main', MainPageView.as_view()),
    path('fomo-view', FomoView.as_view())
]