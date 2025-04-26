from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.getNotes),
    path('notes/create/', views.createNote),
    path('notes/<str:pk>/', views.getNote),

]