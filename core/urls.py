from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('missions/', views.missions, name='missions'),
    path('search/', views.search, name='search'),
    path('missions/<int:mission_id>/', views.mission, name='mission_detail'),
    path('missions/<int:mission_id>/tests/', views.tests, name='tests'),
    path('missions/<int:mission_id>/tests/<int:test_id>/', views.test, name='test_detail'),
]
