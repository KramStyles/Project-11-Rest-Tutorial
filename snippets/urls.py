from django.urls import path

from . import views

urlpatterns = [
    path('serial/', views.ViewApi.as_view(), name='serial'),
    path('sm/', views.ViewModelApi.as_view(), name='serial-model'),

    path('snips/', views.snips),
    path('snip/<int:pk>', views.snip_detail),
]
