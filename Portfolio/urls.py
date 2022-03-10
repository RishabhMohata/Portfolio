from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('project_diabetes', views.project_diabetes, name="project_diabetes"),
    path('project_taxi', views.project_taxi, name="project_taxi"),
    path('project_heart', views.project_heart, name="project_heart"),
    path('project_titanic', views.project_titanic, name="project_titanic"),
    path('titanic_submit', views.titanic_submit, name="titanic_submit"),
    path('diabetes_submit', views.diabetes_submit, name="diabetes_submit"),
    path('taxi_submit', views.taxi_submit, name="taxi_submit"),
    path('heart_submit', views.heart_submit, name='heart_submit'),
]