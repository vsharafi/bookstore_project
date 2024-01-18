from django.urls import path
from . import views



urlpatterns = [
        path('', views.HomePageView.as_view(template_name='home.html'), name='home'),

]