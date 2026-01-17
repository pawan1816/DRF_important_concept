from .models import User
from .serializers import UserSerializer
from rest_framework.generics import  ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle

class UserList(ListAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer
    throttle_classes=[ScopedRateThrottle]


class UserCreate(CreateAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'modifystu'


class UserRetrive(RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'viewstu'


class User_update_api_view(UpdateAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'modifystu'


class User_Destroy_api_view(DestroyAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer
    throttle_classes=[ScopedRateThrottle]
