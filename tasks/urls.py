from django.urls import path
from tasks.views import SurveyAPIView, QuestionAPIView


urlpatterns = [
    path('', SurveyAPIView.as_view()),
    path('question/', QuestionAPIView.as_view())
]