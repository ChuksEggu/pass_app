from django.urls import path
from password_app import views

app_name = 'password_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('recovery/', views.recovery, name='recovery'),

]