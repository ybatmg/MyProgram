from django.urls import path
from .import views

urlpatterns = [
    path('home_index/',views.index,name="index"),
    path('create-task/',views.tasks,name="createtask"),
    path('delete-task/<int:id>',views.deletetask,name="deletetask"),
    path('update-task/<int:id>',views.updatetask,name="updatetask"),
]
