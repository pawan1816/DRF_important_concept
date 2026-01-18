from rest_framework.pagination import CursorPagination

class Mypagination(CursorPagination):
    page_size=4
    ordering = 'passby'
    cursor_query_param='custome_name'

