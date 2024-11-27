from django.urls import path
from . import views

urlpatterns = [
    path('', views.snort_log_view, name='snort_log_view'),
   #path('get_latest_logs/', views.get_latest_logs, name='get_latest_logs'),
]
