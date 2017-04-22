from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        

class ListUsersSerializer(serializers.ListSerializer):

    def validate(self, attrs):
        products_ids = []
        return attrs


class UserStatusSerializer(serializers.Serializer):
    status = serializers.CharField()
    started = serializers.DateTimeField()
    pomodoros = serializers.IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        list_serializer_class = ListUsersSerializer


class TeamStatusSerializer(serializers.Serializer):
    status = serializers.CharField()
    started = serializers.DateTimeField()
    started = serializers.DateTimeField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
