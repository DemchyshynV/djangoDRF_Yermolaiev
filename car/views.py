from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarModel
from .serializers import CarSerializer


class CarView(APIView):
    def get(self, *args, **kwargs):
        # get All
        # car = CarModel.objects.all()
        # serializer = CarSerializer(instance=car, many=True)

        #get one
        # car = CarModel.objects.get(id=2)
        # car = CarModel.objects.get(id=2, model='bmw')
        # serializer = CarSerializer(car)

        #filter
        # cars = CarModel.objects.filter(model__startswith='A')
        # serializer = CarSerializer(instance=cars, many=True)

        cars = CarModel.objects.exclude(id=2)
        serializer = CarSerializer(instance=cars, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        car = self.request.data
        # model = CarModel(**car)
        # model.save()
        CarModel.objects.create(**car)
        return Response('hello from post')

    def put(self, *args, **kwargs):
        CarModel.objects.filter(id=2).update(model='AKA')
        return Response('ok')
    def patch(self, *args, **kwargs):
        return Response('hello from patch')

    def delete(self, *args, **kwargs):
        CarModel.objects.get(id=1).delete()
        return Response('hello from delete')
Create
Read
Update
Delete
