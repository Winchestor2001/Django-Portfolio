from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.PortfolioDetailView.as_view(), name='p_name'),
]