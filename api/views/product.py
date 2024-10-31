from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Product
from ..serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['post'])
    def decrease_quantity(self, request, pk=None):
        product = self.get_object()
        amount = int(request.data.get('amount', 1))

        if product.quantity >= amount:
            product.quantity -= amount
            product.save()
            return Response({'status': 'Количество успешно уменьшено'})
        return Response({'error': 'Недостаточно товара на складе'}, status=400)