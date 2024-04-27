from django.db import models

# Create your models here.

class SurveyResponse(models.Model):
    question_number = models.IntegerField()
    question_type = models.CharField(max_length=20)
    question = models.CharField(max_length=100)
    response = models.TextField()

    def __str__(self):
        return f"Response to question {self.question_number}"
    class Meta:
        app_label = 'SurveyAiApp'

class SurveyQuestion(models.Model):
    question = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question: {self.question[:50]} - Response: {self.response[:50]}"
    class Meta:
        app_label = 'SurveyAiApp'