from django.urls import path
from .import views

urlpatterns = [
    path('<int:pk>',views.newsdetailview.as_view(),name='news-detail'),
    path('', views.pagination.as_view(), name='news'),
]