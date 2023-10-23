from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, CustomViewSet, MessageViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', CustomViewSet, basename='custom')
router.register('', MessageViewSet, basename='message')

urlpatterns = router.urls