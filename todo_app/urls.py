
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:task_id>/',views.update,name='update'),
]
