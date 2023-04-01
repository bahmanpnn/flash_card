from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from core.models import FlashCard
from rest_framework import status
from rest_framework import permissions
from .permissions import *
from .serializers import (
   CreateFlashCardSerializer,
   UpdateFlashCardSerializer,
   ListFlashCardSerializer
   )

# Create your views here.
class CreateFlashCard(APIView):
   permission_classes=(permissions.IsAuthenticated)
   def post(self,request):
      serializer=CreateFlashCardSerializer(data=request.data)

      serializer.is_valid(raise_exception=True)
      serializer.save()

      return Response(serializer.data,status=status.HTTP_201_CREATED)

class UpdateFlashCard(APIView):
   permission_classes=(IsAuthor,IsStaffOrReadOnly)
   def get(self,request,id):
      flash_card=get_object_or_404(FlashCard,id=id)
      serializer=UpdateFlashCardSerializer(flash_card)
      return Response(serializer.data,status=status.HTTP_200_OK)


   def put(self,request,id):
      # req_data=request.data
      # if "id" not in req_data.keys():
         # ... 
         # it means that id it doesn't exists!
      #often we get in args and dont use last line that commented
      
      flash_card=get_object_or_404(FlashCard,id=id)
      serializer=UpdateFlashCardSerializer(data=request.data,instance=flash_card)

      serializer.is_valid(raise_exception=True)
      serializer.save()

      return Response(serializer.data,status=status.HTTP_200_OK)


class DeleteFlashCard(APIView):
   permission_classes=(IsAuthor,IsStaffOrReadOnly)
   def delete(self,request,id):
      flash_card=get_object_or_404(FlashCard,id=id)
      flash_card.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


class ListFlashCard(APIView):
   permission_classes=(IsAuthor,IsStaffOrReadOnly)
   def get(self,request,user_id):
      user_flash_cards=FlashCard.objects.filter(user__id=user_id)
      serializer=ListFlashCardSerializer(user_flash_cards,many=True)
      # serializer.is_valid(raise_exception=True)
      return Response(serializer.data,status=status.HTTP_200_OK)

class ListFlashCardAll(ListAPIView):
   queryset=FlashCard.objects.all()
   serializer_class=ListFlashCardSerializer
   permission_classes=(permissions.IsAuthenticated,)
   
