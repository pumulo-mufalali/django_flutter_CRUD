from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.getNotes),
    path('notes/create/', views.createNote),
    path('notes/<str:pk>/', views.getNote),
    path('notes/<str:pk>/update', views.updateNote),
    path('notes/<str:pk>/delete', views.deleteNote),

]