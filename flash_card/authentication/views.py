from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import CreateUserProfileSerializer
from rest_framework.response import Response


#because of error in saving password with createapiview we should change the codes and set APIView
# if go to admin panel see this error in password field of new user==>
# Invalid password format or unknown hashing algorithm. 

# class CreateUser(CreateAPIView):
#     queryset=User.objects.all()
#     serializer_class=CreateUserProfileSerializer

class CreateUser(APIView):
    def post(self,request):
        req_data=request.data

        serializer=CreateUserProfileSerializer(data=req_data)
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data

        user_data=User(
            username=data['username'],
            email=data['email'],
        )
        user_data.set_password(data['password'])
        user_data.save()

        return Response(serializer.data)