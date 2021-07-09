from rest_framework import status
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CarSerializer, AutoParkSerializer, CarRetriaveSerializer
from .models import CarModel, AutoParkModel


# class CarListCreateView(APIView):
#     def get(self, *args, **kwargs):
#         qs = CarModel.objects.all()
#         serializer = CarSerializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
class CarListCreateView(ListCreateAPIView):
    serializer_class = CarRetriaveSerializer

    # queryset = CarModel.objects.all()

    def get_queryset(self):
        qs = CarModel.objects.all()
        lt = self.request.query_params.get('lt', None)
        if lt:
            qs = qs.filter(year__lt=lt)
        return qs


# class CarRetriveUpdeteDeleteView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#
#         try:
#             instance = CarModel.objects.get(pk=pk)
#         except CarModel.DoesNotExist as err:
#             return Response({'error': str(err)}, status.HTTP_404_NOT_FOUND)
#
#         serializer = CarSerializer(instance)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         data = self.request.data
#         instance = get_object_or_404(CarModel, pk=pk)
#         serializer = CarSerializer(instance, data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         instance = get_object_or_404(CarModel, pk=pk)
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class CarRetriveUpdeteDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarRetriaveSerializer
    queryset = CarModel.objects.all()


class AutoParkList(ListAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
