from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('missions/', views.missions, name='missions'),
    path('search/', views.search, name='search'),
    path('missions/<int:mission_id>/', views.tests, name='tests'),
    path('missions/<int:mission_id>/edit/',
         views.mission_edit, name='mission_edit'),
    path('missions/<int:mission_id>/tests/<int:test_id>/', views.test,
         name='test_detail'),
    # path('missions/<int:mission_id>/tests/<int:test_id>/edit/', 
    #      views.test_edit, name='test_edit'),
]
