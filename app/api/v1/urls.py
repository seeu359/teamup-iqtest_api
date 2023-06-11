from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.CreateTestApiView.as_view(), name='create_test'),
    path('test/detail/', views.RetrieveTestApiView.as_view(), name='test_detail'),
    path('test/iq/', views.CreateIQTestApiView.as_view(), name='iq_save'),
    path('test/eq/', views.CreateEQTestApiView.as_view(), name='eq_save'),
]
