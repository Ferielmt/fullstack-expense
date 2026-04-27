
from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    # List + Create
 path('transactions/all/' , views.TransactionListCreateSimpleView.as_view()),
  # List + Create + Search + Pagination
    path('transactions/', views.TransactionListCreateView.as_view()),
    
    # Retrieve, Update, Delete
    path('transactions/<uuid:id>/', views.TransactionRetrieveUpdateDestroyView.as_view()),
    
    # Optional: Retrieve only
    path('transactions/detail/<uuid:id>/', views.TransactionDetailView.as_view()),
]