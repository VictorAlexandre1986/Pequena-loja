from django.urls import path
from main import views


urlpatterns=[
    path('home/',views.homepage,name='home'),
    path('items/', views.itemspage,name='items')    
]