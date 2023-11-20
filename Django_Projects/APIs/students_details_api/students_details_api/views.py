from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from django.http import JsonResponse

@api_view(['GET','POST'])
def student_list(request):
    # check the request method
    if request.method == 'GET':
        students = Student.objects.all()
        #serialize the students onj you have
        serialized_obj = StudentSerializer(students, many=True)
        return JsonResponse({"students" : serialized_obj.data}, safe = False)
    
    if request.method == 'POST':
        # Deserealize data from passed through request
        student_data = StudentSerializer(data = request.data)
        if student_data.is_valid():
            student_data.save()
            return Response(student_data.data, status=status.HTTP_201_CREATED)
            
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):
    
    try:
        student = Student.objects.get(pk = id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # if student is found
    #check the request method and act accordingly
    if request.method == 'GET':
        # Serialize the student object and return it in Response body return statement
        student_serialized = StudentSerializer(student)
        return Response(student_serialized.data, status=status.HTTP_302_FOUND)
    
    if request.method == 'PUT':
        # get the student details passed from request and deserialize and save it
        student_deserialize = StudentSerializer(student, data=request.data)
        if student_deserialize.is_valid():
            student_deserialize.save()
            return Response(student_deserialize.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
