from .models import Drink
from rest_framework import serializers
from django.http import JsonResponse
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
    
    # check the type of request made
    if request.method == 'GET':
        drinks = Drink.objects.all()
        # Serializing the drinks object
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({"drinks" : serializer.data})
    
    if request.method == 'POST':
        # Deserialize the data get an object that can be stored in database
        serializer = DrinkSerializer(data=request.data)
        # check if serializer is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):

    # check if the item exists in the database
    try:
            drink = Drink.objects.get(pk = id)
    except:
         return Response(status=status.HTTP_404_NOT_FOUND)
    
    # if item is found ...
    # check the request type
    if request.method == 'GET':
        # Serialize the object drink and store it in variable serializer.
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
         # 'PUT' is ued to update the data in the database.
         # deserialize the data to get an object.
         serializer = DrinkSerializer(drink, data = request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
         drink.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)


