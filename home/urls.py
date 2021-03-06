""" Import """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('delivery/', views.DeliveryView.as_view(), name='delivery'),
    path('faqs/', views.FaqsView.as_view(), name='faqs'),
]
