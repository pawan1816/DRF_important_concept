from .models import User
from .serializers import userSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions
from .custompermission import MyPermission
# Authenticated user can access only this api 
class UserModelViewSet0(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes=[IsAuthenticated]

# any once can access this api weather it is aunthicated or not 
class UserModelViewSet1(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes=[AllowAny]


# ONLY is staaf can can use this api 
class UserModelViewSet4(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes=[IsAdminUser]

#any one can read from this api but only the autherized person can write
class UserModelViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]


# the authorization will only  be granted if the  user  is  authenticated  and has the relevent model permission assigned
class UserModelViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

# Similar to the DjangoModelPermissions but  also allows unauthenticated users  to have read-only  access to the api 
class UserModelViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]

# Authentication will only be granted if the user is authenticated  and has  the relevent per-object  permissions and  relevent model permission assigned
class UserModelViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes=[DjangoObjectPermissions]



# Custom Authentication


class UserModelViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes=[MyPermission]