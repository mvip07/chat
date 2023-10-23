from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from .models import UserModel, MessageModel
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, CustomSerializer, MessageSerializer

# Create your views here.

class CustomViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = UserModel.objects.all()
    serializer_class = CustomSerializer

class UserViewSet (ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class MessageViewSet (ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer