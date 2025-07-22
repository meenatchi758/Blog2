from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 👈 add this line
    path('submit/', views.submit_bug, name='submit_bug'),
    path('my/', views.my_bugs, name='my_bugs'),
    path('all/', views.all_bugs, name='all_bugs'),
    path('update/<int:pk>/', views.update_status, name='update_status'),
]
