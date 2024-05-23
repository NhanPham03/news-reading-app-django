from django.contrib.auth import get_user_model
from rest_framework import serializers
from apps.followers.models import Follower

class FollowerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Follower
    fields = '__all__'

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'last_name', 'role']
