from django.urls import path

from todoapp.views import homepage, create, update, TodoDeleteView

urlpatterns = [
    path('', homepage, name='home'),
    path('create/', create, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name='delete'),
]
