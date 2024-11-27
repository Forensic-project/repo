from django.urls import path
from test_xss import views

app_name = 'test_xss' 

urlpatterns = [
    path('test/', views.test_xss, name='test'),
]
