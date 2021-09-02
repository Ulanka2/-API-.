from django.urls import path
from tasks.views import SurveyAPIView, QuestionAPIView


urlpatterns = [
    path('api/v1/survey/', SurveyAPIView.as_view()),
    path('question/', QuestionAPIView.as_view())
]
