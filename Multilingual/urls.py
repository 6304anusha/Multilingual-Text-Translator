from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),            # Homepage with input form
    path('process/', views.process_text, name='process'),  # Form processing and result page
]
