from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'size'   
    page_query_param = 'page'

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 100
    limit_query_param = 'limit'     # default
    offset_query_param = 'offset'   # default