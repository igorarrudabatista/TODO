from django.urls import path, include
from .views import  TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView
from .views import CustomLoginview, RegisterPage, ProfilePage

from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('login/', CustomLoginview.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('profile/', ProfilePage.as_view(), name='profile'),


    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)