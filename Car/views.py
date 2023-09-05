from rest_framework.views import APIView
from . models import Car
from . serializers import CarSerializer
from rest_framework.response import Response


class SelectCarView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                data = Car.objects.get(pk=pk)
                serializer = CarSerializer(data, context={'request': request}, many=False)
                return Response(serializer.data)
            except:
                return Response(f"ID {pk} Not found")
        data = Car.objects.all()
        serializer = CarSerializer(data, context={'request': request}, many=True)
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
