from django.urls import path
from . import views
urlpatterns = [
    path('admission', views.admission, name='admission'),

    path('courses', views.courses, name='courses'),

    path('course-single', views.course_single, name='course-single'),
   
    path('news-single', views.news_single, name='news-single'),
    path('news_single/<slug>', views.news_single, name="news_single"),


]