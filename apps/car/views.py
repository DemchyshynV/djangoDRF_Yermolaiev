from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from .serializers import AutoParkSerializer, CarRetriaveSerializer
from core.models import CarModel, AutoParkModel


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarRetriaveSerializer

    def get_queryset(self):
        qs = CarModel.objects.all()
        lt = self.request.query_params.get('lt', None)
        if lt:
            qs = qs.filter(year__lt=lt)
        return qs


class CarRetriveUpdeteDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarRetriaveSerializer
    queryset = CarModel.objects.all()


class AutoParkList(ListAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
