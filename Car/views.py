from rest_framework.views import APIView
from . models import Car
from . serializers import CarSerializer
from rest_framework.response import Response

from .utils import Redis


class SelectCarView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                cache_data = Redis.get('CarAPICall') #
                if cache_data:
                    return Response(cache_data)
                data = Car.objects.get(pk=pk)
                serializer = CarSerializer(data, context={'request': request}, many=False)
                Redis.set("CarAPICall", serializer.data)
                return Response(serializer.data)
            except:
                return Response(f"ID {pk} Not found")
        cache_data = Redis.get('CarAPICall')
        if cache_data:
            return Response(cache_data)

        data = Car.objects.all()
        serializer = CarSerializer(data, context={'request': request}, many=True)
        Redis.set("CarAPICall", serializer.data)
        return Response(serializer.data)


class AddCarVIew(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return serializer.errors


class DeleteCarView(APIView):
    def delete(self, request, pk):
        event = Car.objects.get(pk=pk)
        event.delete()
        return Response("Deletion Successful")
