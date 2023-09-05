from rest_framework.views import APIView
from . models import Animal
from . serializers import AnimalSerializer
from rest_framework.response import Response


class SelectAnimalView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                data = Animal.objects.get(pk=pk)
                serializer = AnimalSerializer(data, context={'request': request}, many=False)
                return Response(serializer.data)
            except:
                return Response(f"ID {pk} Not found")
        data = Animal.objects.all()
        serializer = AnimalSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)


class AddAnimalVIew(APIView):
    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return serializer.errors


class DeleteAnimalView(APIView):
    def delete(self, request, pk):
        event = Animal.objects.get(pk=pk)
        event.delete()
        return Response("Deletion Successful")
