from rest_framework.routers import DefaultRouter
from ..viewsets.task_viewsets import TaskViewSet


router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

