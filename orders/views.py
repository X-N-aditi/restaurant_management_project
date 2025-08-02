from django.shortcuts import render

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer

class OrderCreateView(APIView):
    def post(self, request):
        try:
            serializer = OrderSerializer(data=request.data)
        except OrderSerializer.DoesNotExist:
            return Response({'error': 'Order detail not found'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            order = serializer.save()
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

