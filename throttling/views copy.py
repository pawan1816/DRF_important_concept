from .models import User
from .serializers import userSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from throttling.throttling import Pawan_Rate_Throttle
# Authenticated user can access only this api 
class UserModelViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes={AnonRateThrottle,UserRateThrottle}


class UserModelViewSet1(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes={AnonRateThrottle,Pawan_Rate_Throttle}




