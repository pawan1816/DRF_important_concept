from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'student_api', StudentViewSet, basename='student')

urlpatterns = router.urls
