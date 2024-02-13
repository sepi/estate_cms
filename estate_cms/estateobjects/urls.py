from django.urls import path
# from django.conf.urls.i18n import i18n_patterns
from .views import EstateObjectDetailView, place_bid

# app_name = 'estateobjects'
urlpatterns = [
    path('<int:pk>/', EstateObjectDetailView.as_view(), name='detail'),
    path('<int:pk>/place_bid', place_bid, name='place_bid'),
]
