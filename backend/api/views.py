from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination, Response
from .models import Transaction
from .serializers import TransactionSerializer


# Pagination Class

class TransactionPagination(PageNumberPagination):
    page_size = 1
 # Allow to control page size via URL query like this ?page_size=10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'total_items': self.page.paginator.count,          # total number of items
            'total_pages': self.page.paginator.num_pages,      # total pages
            'current_page': self.page.number,                  # current page
            'page_size': self.get_page_size(self.request),     # items per page
            'next': self.get_next_link(),                      # next page URL
            'previous': self.get_previous_link(),              # previous page URL
            'results': data                                    # actual data
        })


# SIMPLE VERSION (no search, no pagination)
class TransactionListCreateSimpleView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# ADVANCED VERSION (search + pagination)
class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']
    pagination_class = TransactionPagination


# Retrieve / Update / Delete
class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "id"

# Retrieve ONLY (Detail View) 
class TransactionDetailView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "id"