from django.contrib.auth.models import Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer
from api.model import Pomodoro


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Pomodoro.objects.all()
    serializer_class = UserStatusSerializer

    def retrieve(self, request, *args, **kwargs):

        return super(UserStatusViewSet, self).retrieve(
            request, *args, **kwargs)
 
 
class GroupStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Pomodoro.objects.all()
    serializer_class = GroupStatusSerializer

    def retrieve(self, request, *args, **kwargs):

        return super(GroupStatusViewSet, self).retrieve(
            request, *args, **kwargs)

