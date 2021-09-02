from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from tasks.models import Survey, Question, Choice, Answer
from tasks.serializers import SurveySerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer

class SurveyAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        survey = Survey.objects.all()
        serializers = SurveySerializer(survey, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = SurveySerializer(data=request.data )
        if serializer.is_valid():
            owner = request.user
            survey = Survey.objects.create(
            owner=owner,
            survey_name=serializer.validated_data.get('survey_name'),
            end_date=serializer.validated_data.get('end_date'),
            survey_description=serializer.validated_data.get('survey_description'),

            )
            serializer = SurveySerializer(instance=survey)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        survey = get_object_or_404(Survey, id=id)
        survey.delete()
        return Response({'detail': 'deleted'}, 
        status=status.HTTP_204_NO_CONTENT)


    def put(self, request, id):
        survey = get_object_or_404(Survey, id=id)
        serializer = SurveySerializer(data=request.data )
        if serializer.is_valid():
            update_fields = []
            for fields, value in serializer.validated_data.items():
                setattr(survey, fields, value)
                update_fields.append(fields)
            survey.save(update_fields=update_fields)
            
            serializer = SurveySerializer(instance=survey)
            return Response(serializer.data)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class QuestionAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        question = Question.objects.all()
        serializers = QuestionSerializer(question, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data )
        if serializer.is_valid():
            owner = request.user
            question= Question.objects.create(
            owner=owner,
            survey=serializer.validated_data.get('survey'),
            question_text=serializer.validated_data.get('question_text'),
            question_type=serializer.validated_data.get('question_type'),
            )
            serializer = QuestionSerializer(instance=question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        question = get_object_or_404(Question, id=id)
        question.delete()
        return Response({'detail': 'deleted'}, 
        status=status.HTTP_204_NO_CONTENT)


    def put(self, request, id):
        question = get_object_or_404(Question, id=id)
        serializer = QuestionSerializer(data=request.data )
        if serializer.is_valid():
            update_fields = []
            for fields, value in serializer.validated_data.items():
                setattr(question, fields, value)
                update_fields.append(fields)
            question.save(update_fields=update_fields)
            
            serializer = QuestionSerializer(instance=question)
            return Response(serializer.data)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
