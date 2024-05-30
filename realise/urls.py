from django.urls import path
from .import views

urlpatterns = [
    path('<int:pk>',views.realisedetailview.as_view(),name='realise-detail'),
    path('', views.pagination4.as_view(), name='realise'),
]