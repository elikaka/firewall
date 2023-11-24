from django.urls import path
# Create your tests here.
from . import views

urlpatterns = [
    path('',views.form_view, name='form_view'),
    path('submit/', views.form_submission, name='form_submission'),
]