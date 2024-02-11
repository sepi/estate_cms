from django.urls import path
from .views import EstateObjectDetailView

# app_name = 'estateobjects'
urlpatterns = [
    path('<int:pk>/', EstateObjectDetailView.as_view(), name='detail'),
]
