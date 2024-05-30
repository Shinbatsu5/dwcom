from django.urls import path
from .import views

urlpatterns = [
    path('<int:pk>',views.partnersdetailview.as_view(),name='partners-detail'),
    path('', views.pagination5.as_view(),name='partners'),
]