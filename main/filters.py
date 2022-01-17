from django_filters import rest_framework as filters
from .models import Hotel


class HotelFilter(filters.FilterSet):
    price_from = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Hotel
        fields = ['category']


class HotelRatingFilter(filters.FilterSet):
    rating_from = filters.NumberFilter(field_name='rating', lookup_expr='gte')
    rating_to = filters.NumberFilter(field_name='rating', lookup_expr='lte')

    class Meta:
        model = Hotel
        fields = ['category']


# class HotelFilter(filters.FilterSet):
#     arrival_from = filters.NumberFilter(field_name='arrival_date', lookup_expr='gte')
#     departure_to = filters.NumberFilter(field_name='departure_date', lookup_expr='lte')
#
#     class Meta:
#         model = Room
#         fields = ['booking']


