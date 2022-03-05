from django.urls import path
from .views import delete_data, show_home,show_update
urlpatterns = [
    path('add/', show_home,name='addandshow'),
    path('update/',show_update,name='updateandshow'),
    path('delete/<int:id>',delete_data,name='delete')
]
