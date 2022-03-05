from django.urls import path
from .views import delete_data, show_home,update_data
urlpatterns = [
    path('add/', show_home,name='addandshow'),
    path('delete/<int:id>',delete_data,name='delete'),
    path('<int:id>/',update_data,name='update'),
]
