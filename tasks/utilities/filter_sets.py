import django_filters
from ..models import CustomUser

class UserFilter(django_filters.FilterSet):
    id = django_filters.BaseInFilter(field_name='id', lookup_expr='in')
    username = django_filters.BaseInFilter(field_name='username', lookup_expr='in')
    emaail = django_filters.CharFilter(field_name='email', lookup_expr='exact')

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']
