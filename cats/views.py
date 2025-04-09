from rest_framework import generics

from .models import Cat
from .serializers import CatSerializer


class CatList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from .models import Cat
# from .serializers import CatSerializer


# class APICat(APIView):
#     def get(self, request):
#         cats = Cat.objects.all()
#         serializer = CatSerializer(cats, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         # Проверяем, является ли входящие данные списком
#         if isinstance(request.data, list):
#             # Если это список, используем параметр many=True
#             serializer = CatSerializer(data=request.data, many=True)
#         else:
#             # Если это одиночный объект
#             serializer = CatSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'POST'])  # Применили декоратор и указали разрешённые методы
# def hello(request):
#     # По задумке, в ответ на POST-запрос нужно вернуть JSON с теми данными, 
#     # которые получены в запросе.
#     # Для этого в объект Response() передаём словарь request.data. 
#     if request.method == 'POST':
#         return Response({'message': 'Получены данные', 'data': request.data})

#     # В ответ на GET-запрос нужно вернуть JSON
#     # Он тоже будет создан из словаря, переданного в Response()
#     return Response({'message': 'Это был GET-запрос!'})
