from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('url/', views.Convert_url,name="short_url"), 
    path('task1/<str:url_code>/', views.redirecting, name='redirecting')
]