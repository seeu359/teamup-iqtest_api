from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.CreateTestApiView.as_view()),
    path('test/detail/', views.RetrieveTestApiView.as_view()),
    path('test/iq/', views.CreateIQTestApiView.as_view()),
    path('test/eq/', views.CreateEQTestApiView.as_view()),
]
