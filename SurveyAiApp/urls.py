from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('generatehealthcarequestions/', views.generate_healthcare_questions_json, name='generate_healthcare_questions_json'),
    path('storehealthcareanswers/',views.store_healthcare_answers, name='store_healthcare_answers'),
    path('hospitality_travel_questions/',views.generate_hospitality_travel_json, name='generate_hospitality_travel_json'),
    path('store_hospitality_travel_answers/', views.store_hospitality_travel_answers, name='store_hospitality_travel_answers'),
    path('generate_education_questions_json/',views.generate_education_questions_json, name='generate_education_questions_json'),
    path('generate_employee_satisfaction_questions_json/',views.generate_employee_satisfaction_questions_json, name='generate_employee_satisfaction_questions_json'),
    path('sentiment_analysis/', views.calculate_sentiment_percentage, name='sentiment_analysis'),
    path('survey_view/',views.survey_view, name='survey_view'),
    path('chat_with_gpt/', views.chat_with_gpt_view, name='chat_with_gpt'),
    path('ai_generated_questions/', views.my_view_function, name='my_view'),   
    path('starter_temp/', views.starter_temp),
    path('customer_satisfaction/', views.customer_satisfaction, name='customer_satisfaction'),
    path('survey_preview/',views.survey_preview), 
    path('healthcarequestions/',views.healthcarequestions), 
    path('builtwithscratch/', views.buildWithScratch, name='buildwithscratch'),
    path('buildwith_ai/', views.buildwithAi, name='buildwith_ai'),
    path('ai_preview/', views.ai_preview, name='ai_preview'),
    path('users/',views.project_users),
] 