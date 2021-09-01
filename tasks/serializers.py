from rest_framework import serializers
from django.contrib.auth import get_user_model

from tasks.models import Survey, Question, Choice, Answer


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', ]


class SurveySerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)

    class Meta:
        model = Survey
        fields = ['id', 'owner', 'survey_name', 'pub_date', 'end_date', 'survey_description', ]
        read_only_fields = ['pub_date', ]


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['question_text', 'question_type', ]


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['question', 'choice_text', ]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['user_id', 'choice_text', ]
        