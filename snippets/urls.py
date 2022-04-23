from django.urls import path

from . import views

urlpatterns = [
    path('serial/', views.ViewApi.as_view(), name='serial')
]
