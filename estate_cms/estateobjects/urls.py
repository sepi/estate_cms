from django.urls import path
from estate_cms.estateobjects.views import EstateObjectDetailView, place_bid

# app_name = 'estateobjects'
urlpatterns = [
    path('<int:pk>/', EstateObjectDetailView.as_view(), name='detail'),
    path('<int:pk>/place_bid', place_bid, name='place_bid'),
]
