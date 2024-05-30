from django.urls import path
from. import views


urlpatterns = [
    path('',views.pagination6.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('injsystem', views.injsystem, name='injsystem'),
    path('licenses', views.licenses, name='licenses'),
    path('projectsupplies', views.projectsupplies, name='projectsupplies'),
    path('requisites', views.requisites, name='requisites'),
    path('vakansii', views.vakansii, name='vakansii'),
    path('news', views.news , name='news'),
    path('realise', views.realise, name='realise'),
    path('partners', views.partners, name='partners'),
]


