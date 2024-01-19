from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index,  name='log'),
    path('todo', views.todo, name = 'todo'),
    path('create-aplctn', views.create, name = 'create'),
    path('aplctn', views.aplctn, name = 'aplctn'),
    path('todo/<str:title>', views.ApplicationDetailView.as_view(), name='detail'),
    path('logout/', LogoutView.as_view(next_page='log'), name='logout'),
    path('desk/<int:pk>/delete/', views.delete_desk, name='delete_desk'),
    path('change-status/<int:pk>/', views.change_status, name='change_status'),
]
