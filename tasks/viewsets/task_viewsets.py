from rest_framework import viewsets, permissions
from accounts.models import CustomUser
from rest_framework.decorators import action
from ..models import Task
from ..serializers.task_serializer import TaskListSerializer, TaskRetriveSerializer, TaskWriteSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters .rest_framework import DjangoFilterBackend
from tasks.utilities.permissions import IsAssignedUserOrAdmin, IsAdmin

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = {
        'status',
        'due_date'
    }

    def get_permissions(self):
        if self.request.method in ['POST', 'DELETE', 'PUT']:
            return [IsAdmin()]
        if self.request.method == ['GET','PATCH']:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Task.objects.all()
        return Task.objects.filter(assigned_to=user)
    
    def perform_create(self, serializer):
        serializer.save()

    @action(detail=True, methods=['patch'], permission_classes=[permissions.IsAuthenticated, IsAssignedUserOrAdmin])
    def status(self, request, pk=None):
        task = self.get_object()
        new_status = request.data.get('status')

        if not new_status:
            return Response({"error": "Status is required."}, status=status.HTTP_400_BAD_REQUEST)

        if new_status == 'completed' and task.due_date < date.today() and request.user.role != 'admin':
            return Response({"error": "Cannot complete overdue task without admin."}, status=status.HTTP_403_FORBIDDEN)

        task.status = new_status
        task.save()
        return Response({"message": "Status updated", "status": task.status})
    
    def get_serializer_class(self):
        if self.action in ['create', 'update''partial_update']:
            return TaskWriteSerializer
        elif self.action == 'retrive':
            return TaskRetriveSerializer
        return super().get_serializer_class()