from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pl>/',views.DetailView.as_view(),name='detail'),
]