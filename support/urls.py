from rest_framework.routers import DefaultRouter
from .views import UserViewSet, InteractionViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('interactions', InteractionViewSet)

urlpatterns = router.urls
