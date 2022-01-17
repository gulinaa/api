
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]

    @action(methods=['GET'], detail=False)
    def history(self, request):
        guest = request.user
        queryset = self.queryset.filter(guest=guest)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
