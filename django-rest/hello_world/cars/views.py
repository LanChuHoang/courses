from rest_framework import generics, permissions

from .models import CarModel
from .serializers import CarSerializer


class CarListAPI(generics.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]
