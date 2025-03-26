import django_filters

from main.models import Book


class BookFilter(django_filters.FilterSet):
    """
    Filter for Book objects.
    """
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author', lookup_expr='icontains')
    genre = django_filters.CharFilter(field_name='genre', lookup_expr='icontains')
    publication_year = django_filters.NumberFilter(field_name='publication_year', lookup_expr='exact')
    publication_year_lte = django_filters.NumberFilter(field_name='publication_year', lookup_expr='lte')
    publication_year_gte = django_filters.NumberFilter(field_name='publication_year', lookup_expr='gte')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'genre']
