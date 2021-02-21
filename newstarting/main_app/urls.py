from django.urls import path
from . import views

urlpatterns = [
    path('',views.newstartingView,name='home'),
    path('home/',views.newstartingView,name='home')

]