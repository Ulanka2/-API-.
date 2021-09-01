from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from tasks.models import Survey, Question, Choice, Answer
from tasks.serializers import SurveySerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer


class SurveyView(viewsets.ModelViewSet):
    queryset = Survey.objects.all().order_by('-id')
    serializer_class = SurveySerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

