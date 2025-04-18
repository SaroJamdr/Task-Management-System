import django_filters
from ..models import Task

class UserFilter(django_filters.FilterSet):
    id = django_filters.BaseInFilter(field_name='id', lookup_expr='in')
    title = django_filters.BaseInFilter(field_name='username', lookup_expr='in')

    class Meta:
        model = Task
        fields = ['id', 'username', 'email']
