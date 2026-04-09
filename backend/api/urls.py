from django.urls import path
from . import views

urlpatterns = [
    path('ask/', views.ask_question),

    path('conversations/', views.get_conversations),
    path('conversations/<int:pk>/', views.get_conversation),

    path('conversations/<int:pk>/update/', views.update_conversation),
    path('conversations/<int:pk>/delete/', views.delete_conversation),
]