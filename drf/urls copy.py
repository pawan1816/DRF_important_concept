# -------------------------------------------------

# normal filter then drf filter


# ==================================================


# from django.contrib import admin
# from django.urls import path
# from filter_drf import views


# urlpatterns = [
#     path('admin/',admin.site.urls),
#     path('studentapi/',views.StudentList.as_view())
# ]


# -------------------------


# search filter


# ---------------------------




# from django.contrib import admin
# from django.urls import path
# from searchfilter import views


# urlpatterns = [
#     path('admin/',admin.site.urls),
#     path('studentapi/',views.StudentList.as_view())
# ]



# -----------------------------------------------


# pagination


# --------------------------------------


from django.contrib import admin
from django.urls import path
from paginationsapp import views


urlpatterns = [
    path('admin/',admin.site.urls),
    path('studentapi/',views.StudentList.as_view())
]














# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# # from viewSet_DRF.views import StudentViewSet
# # from modelViewset.views import StudentModelViewSet,
# # from modelViewset.views import StudentReadOnlyModelViewSets
# # from authentication import views
# # from sessionAuthentication import views
# # from tokenAuthentication import views
# # from rest_framework.authtoken.views import obtain_auth_token
# # from tokenAuthentication.auth import GetTokenView
# from throttling import views
# router = DefaultRouter()
# # router.register(r'student_api', StudentViewSet, basename='student')
# # router.register(r'student_api', StudentReadOnlyModelViewSets, basename='student')
# # router.register(r'authentication',views.UserModelViewSet,basename='student_authentication')
# router.register(r'authentication',views.UserModelViewSet,basename='student_authentication'),
# router.register(r'authentication1',views.UserModelViewSet1,basename='student_authentication1'),


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('student/', include(router.urls)),
#     path('auth/',include('rest_framework.urls', namespace="rest_framework")),
#     # path('gettoken/',GetTokenView.as_view())
# ]




# -----------------------------------


# THROTLLING APPLYING FOR THE MULTIPLE CLASS WITH DIFFERENT THROTTLING VALUES

# ------------------------------------


# from django.contrib import admin
# from django.urls import path
# from throttling import views


# urlpatterns = [
#     path('admin/',admin.site.urls),
#     path('studentlist/', views.UserList.as_view()),
#     path('studentscreate/', views.UserCreate.as_view()),
#     path('studentsretrive/<int:pk>/', views.UserRetrive.as_view()),
#     path('studentsupdate/<int:pk>/', views.User_update_api_view.as_view()),
#     path('studentsdestroy/<int:pk>/', views.User_Destroy_api_view.as_view()),
# ]




# ___________________________

# for the auth token permission
    
# ____________________________

# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from tokenAuthentication.views import UserModelViewSet

# router = DefaultRouter()
# router.register(r'authentication', UserModelViewSet, basename='authentication')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('student/', include(router.urls)),
# ]



# -----------------------------


# this is for the 3rd party api

# ----------------------------


# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from thirdparty_authentication.views import UserModelViewSet
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )


# router = DefaultRouter()
# router.register(r'authentication', UserModelViewSet, basename='authentication')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('student/', include(router.urls)),
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('varifyToken/',TokenVerifyView.as_view(), name= 'token_verify')
# ]




# ---------------------------------------------

# fitering and django filter


# ---------------------------------------------

