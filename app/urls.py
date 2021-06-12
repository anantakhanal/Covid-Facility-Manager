from django.contrib import admin
from django.urls import path, include
from . import views
from app.views import HospitalDetailView

urlpatterns = [
    path('',views.home ,name='homepage'),
    path('hospital/<int:pk>', HospitalDetailView.as_view(), name='hospital_detail'),
]
