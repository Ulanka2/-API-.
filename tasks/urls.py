from django.urls import path
from rest_framework.routers import SimpleRouter

from tasks.views import SurveyView

router = SimpleRouter()
router.register('tasks', SurveyView)
urlpatterns = []

urlpatterns += router.urls