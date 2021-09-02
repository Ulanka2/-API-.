from django.urls import path
from tasks.views import SurveyAPIView, QuestionAPIView


urlpatterns = [
    path('', SurveyAPIView.as_view()),
    path('question/', QuestionAPIView.as_view()),
    # path('<int:id>/detail/', TaskDetailGenericView.as_view()),
    # path('<int:id>/update',  TaskUpdateGenericView.as_view()),
    # path('<int:id>/destroy',  TaskDestroyGenericView.as_view()),

]