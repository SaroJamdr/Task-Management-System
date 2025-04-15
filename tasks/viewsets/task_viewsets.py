from rest_framework import viewsets, permissions
from accounts.models import CustomUser
from ..models import Task
from ..serializers.task_serializer import TaskSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters .rest_framework import DjangoFilterBackend

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['-id']

    # filterset_fields = {
    #     'id': ['exact', 'gt', 'lt', 'gte', 'lte'],
    #     'created_date': ['exact','gte', 'lte'],
    #     'title': ['exact', 'in'],
    # }


    def get_permissions(self):
        if self.action in ['create']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
    
    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.all() if user.role == 'admin' else Task.objects.filter(assigned_to=user)

        status = self.request.query_params.get('status')
        due_date = self.request.query_params.get('due_date')

        if status:
            queryset = queryset.filter(status=status)
        if due_date:
            queryset = queryset.filter(due_date=due_date)

        return queryset