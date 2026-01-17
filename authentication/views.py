from .models import User
from .serializers import userSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

# Authenticated user can access only this api 
class UserModelViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes=[IsAuthenticated]

# any once can access this api weather it is aunthicated or not 
class UserModelViewSet1(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes=[AllowAny]


# ONLY is staaf can can use this api 
class UserModelViewSet4(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes=[IsAdminUser]
