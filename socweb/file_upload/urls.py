from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('result/', views.output_data, name='output_data'),
    #path('dataout/', views.output_data, name='output_data'),
    path('test/', views.test_content, name='test_content'),
]
